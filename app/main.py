
"""Initialize app."""
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from model import db
import api
import logging
from config import Config
import argparse
import sys
import os

flask_app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = ''
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
flask_app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# Setting log configuration
logging.basicConfig(filename='log.txt', filemode="a+", level=os.environ.get('LOG_LEVEL', logging.INFO),
                    format='[%(asctime)s]-[%(name)s]-[%(levelname)s]-%(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')


def main():

    flask_app.config['SQLALCHEMY_ECHO'] = False
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['CORS_HEADERS'] = 'X-Requested-With, Content-Type'
    db.init_app(flask_app)
    db.create_all(app=flask_app)
    print("flask")
    flask_app.register_blueprint(api.bp)
    flask_app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
