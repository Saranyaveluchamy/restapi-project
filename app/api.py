import json

from model import db, car_details
from flask import Blueprint, request, jsonify, make_response
from datetime import datetime
import re
from flask import abort
import pandas as pd
import Levenshtein
import logging
import os

bp = Blueprint('insert_bp', '')


logger = logging.getLogger("api")


@bp.route('/plate', methods=['POST'])
def insert_car_plate_details():
    """
    This is the api to insert the car plate number
    Call this api passing a cat plate name and get the response
    data:
      - plate: M-BT_134
    responses:
      200:
        message: car plate number {} added to database successfully
      400:
        message: Key name plate is missing in json
      422:
         message: Not a valid germany car plate number

    """

    try:
        print("started the insertion")
        get_data = request.json
        if "plate" in get_data:
            plate_number = get_data['plate']
            if plate_number:
                pattern = re.compile(
                    "[A-z]{1,4}-[A-Z]{1,2}(?<!\d)[1-9]\d{0,3}(?!\d)")
                if pattern.match(plate_number):
                    car_plate_details = car_details(
                        car_number_plate=plate_number,
                        country='Germany',
                        inserted_on=datetime.today()
                    )
                    db.session.add(car_plate_details)
                    db.session.commit()
                    logger.info(
                        "car plate number {} added to database successfully!".format(plate_number))
                    return make_response(jsonify({'message': 'car plate number added to database successfully!'}))
                else:
                    status_code = 422
                    raise Exception
        if not "plate" in get_data:
            status_code = 400
            raise Exception
    except Exception as exe:
        if status_code == 400:
            logger.info("Key name plate is missing")
            return abort(status_code, 'Key name plate is missing in data')
        if status_code == 422:
            logger.info("Not a valid germany car plate number")
            return abort(status_code, 'Not a valid germany car plate number')
        else:
            logger.error("Error in adding the car details" +
                         str(exe), exc_info=True)


@bp.route('/plate', methods=['GET'])
def fetch_car_plate_details():
    """
    This is the api to get  the car details
    Call this api to get all the car details
    method:
      GET
    response:
      200

    """
    try:
        print("get car plate details")
        logger.info("call for fetching the car details")
        get_car_plate_details = db.session.query(car_details.car_id,
                                                 car_details.car_number_plate,
                                                 car_details.country,
                                                 car_details.inserted_on).all()
        db.session.commit()
        output_car_plate = []
        if get_car_plate_details:
            for car in get_car_plate_details:
                output_car_plate.append({
                    'plate': car.car_number_plate,
                    'timestamp': car.inserted_on.strftime("%Y-%m-%dT%H:%M:%SZ")
                })
            return jsonify({'car_details': output_car_plate})
        else:
            return jsonify({"message": "No data"})

    except Exception as exe:
        logger.error("Error in fetching the car details" +
                     str(exe), exc_info=True)
        return make_response(jsonify({'messsage': 'Error in fetching the car details'}))


@bp.route('/search-plate', methods=['GET'])
def search_car_plate_details():
    """
    This is the api to search the particular car details
    method:
      GET
    param:
        -key=MDFV123
        -levenshtein=1
    response:
      200
    """
    try:
        print("get car plate details")
        logger.info("search the car plate details in database")
        search_key = request.args.get('key', None).strip()
        levenshtein = int(request.args.get('levenshtein', None).strip())
        data = search_key.replace('-', '')
        get_car_plate_details = db.session.query(car_details.car_id,
                                                 car_details.car_number_plate,
                                                 car_details.country,
                                                 car_details.inserted_on).all()
        db.session.commit()
        if len(get_car_plate_details) > 0:
            df = pd.DataFrame(get_car_plate_details, columns=[
                              'car_id', 'plate', 'country', 'timestamp'])
            df['plate'] = df['plate'].str.replace('-', '')
            print(df.shape)
            df['distance'] = df.apply(
                lambda x: Levenshtein.distance(x['plate'], data), axis=1)
            df = df.loc[(df['distance'] <= levenshtein)]
            print(df.shape)
            result = []
            print(df.empty)
            if df.empty:
                return jsonify({"message": "No data"})
            else:
                for index, row in df.iterrows():
                    result.append({
                        'plate': row['plate'],
                        'timestamp': row['timestamp'].strftime("%Y-%m-%dT%H:%M:%SZ")
                    })
                return jsonify({data: result})

    except Exception as exe:
        logger.error("search car details failed " + str(exe), exc_info=True)
        return make_response(jsonify({'messsage': 'Error!!'}))
