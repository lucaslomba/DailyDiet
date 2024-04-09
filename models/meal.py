from database import db
from flask_login import UserMixin

class Meal(db.Model, UserMixin):
    # id (int), username (text), password (text), role (text)
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    is_diet = db.Column(db.Boolean, nullable=False)
