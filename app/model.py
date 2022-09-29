from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# Database ORMs
class car_details(db.Model):
    __tablename__ = 'tbl_car_details'
    car_id = db.Column('car_id', db.Integer,
                       primary_key=True, autoincrement=True)
    car_number_plate = db.Column(
        'car_number_plate', db.String(250), nullable=False)
    country = db.Column('country', db.String(100), nullable=False)
    inserted_on = db.Column('inserted_on', db.DateTime(), nullable=False)
