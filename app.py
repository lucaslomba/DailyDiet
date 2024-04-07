from flask import Flask
from database import db

from models.user import User
from models.meal import Meal

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/dailydiet'

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
