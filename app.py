from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import Flask, request, jsonify
from database import db
import datetime
import bcrypt

from models.user import User
from models.meal import Meal

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/dailydiet'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'login'

## LOGIN AND LOGOUT METHODS

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)
            return jsonify({"message": "Autenticação realizada com sucesso"})
        
    return jsonify({"message": "Credenciais inválidas"}), 400

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizada com sucesso"})

## USER METHODS

@app.route('/user', methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuario cadastrado com sucesso"})

    return jsonify({"message": "Dados inválidas"}), 400

@app.route('/user', methods=["GET"])
@login_required
def read_meals():
    meals = Meal.query.filter_by(id_user=current_user.id).all()
    
    if meals:
        return jsonify(meals)

    return jsonify({"message": "Rota em desenvolvimento"}), 500

## MEALS METHODS
@app.route('/meal', methods=["POST"])
@login_required
def create_meal():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    is_diet = data.get("is_diet")

    if name and description and is_diet:
        meal = Meal(id_user=current_user.id, name=name, description=description, date_time=datetime.datetime.now(), is_diet=bool(is_diet))
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refeição cadastrada com sucesso"})

    return jsonify({"message": "Dados inválidas"}), 400

@app.route('/meal/<int:id_meal>', methods=["PUT"])
@login_required
def update_meal(id_meal):
    return jsonify({"message": "Rota em desenvolvimento"}), 500

@app.route('/meal/<int:id_meal>', methods=["GET"])
@login_required
def read_meal(id_meal):
    return jsonify({"message": "Rota em desenvolvimento"}), 500

@app.route('/meal/<int:id_meal>', methods=["DELETE"])
@login_required
def delete_meal(id_meal):
    return jsonify({"message": "Rota em desenvolvimento"}), 500


if __name__ == '__main__':
    app.run(debug=True)
