from flask import Blueprint, request, jsonify
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user, current_user
from flask_cors import CORS
from werkzeug import exceptions
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt

from flourish_app.extensions import db
from flourish_app.models import Products, Users, Category


main = Blueprint('main', __name__) 
CORS(main)


# bcrypt = Bcrypt(main)
login_manager = LoginManager(main)
login_manager.init_app(main)
login_manager.login_view = "login" #our app and flask login to work together

@main.route("/")
def hello():
    return "Hello World!"

@login_manager.user_loader #used to reload object from user id stored in session
def load_user(user_id):
    return Users.query.get(int(user_id))

#working
@main.route("/login", methods = ['POST', "GET"])
def login():
    req = request.get_json()
    user = Users.query.filter_by(email = req['email']).first()
    if user:
        if check_password_hash(user.passwrd, req['passwrd']):
            login_user(user)
        return f"Login sucessful!", 200
            
#working
@main.route("/register", methods = ['POST', "GET"])
def register():
    req = request.get_json()
    hashed_password = generate_password_hash(req['passwrd'])
    new_user =  Users(
        username = req['username'], 
        passwrd = hashed_password, 
        email = req['email'],
        rating = 0, 
        rating_num = 0, 
        location = 'ABCD', 
        radius = 2
    )
    db.session.add(new_user)
    db.session.commit()
    return f"New user was added!", 201
        
# needs fixing
@main.route('/logout', methods = ["GET", "POST"])
@login_required
def logout():
    logout_user  
    return f"Logged out sucessfully!", 201

#working
@main.route('/products', methods=['GET','POST'])
def getAllProducts():
    if request.method == 'GET':
        try: 
            allProducts = Products.query.all()
            return  jsonify([e.serialize() for e in allProducts])
        except exceptions.NotFound:
            raise exceptions.NotFound("There are no products to view at the moment!")
        except:
            raise exceptions.InternalServerError()

    elif request.method == 'POST':
    # format of request 
    # { "user_id": 1, "description": "Tomatoes", "category_id": 2, "is_retail": "True", "location": "SE18", "price": 2.99, "expiry": "02/04/2022", "image": "LINK"}
        try:
            req = request.get_json()
            new_product = Products(
                user_id = req['user_id'],
                description = req['description'], 
                category_id = req['category_id'],
                is_retail = req['is_retail'], 
                location = req['location'], 
                price = req['price'], 
                expiry = req['expiry'], 
                image = req['image']
            )
            db.session.add(new_product)
            db.session.commit()
            return f"New product was added!", 201

        except: 
            raise exceptions.InternalServerError()

#working
@main.get('/products/<int:product_id>')
def getProductById(product_id):
    try: 
        product = Products.query.get_or_404(product_id)
        return  jsonify([product.serialize()])
    except exceptions.NotFound:
        raise exceptions.NotFound("Product not found!")
    except:
        raise exceptions.InternalServerError()

@main.route('/users', methods=['GET','POST'])
def getAllUsers():
    if request.method == 'GET':
        try: 
            allUsers = Users.query.all()
            return  jsonify([e.serialize() for e in allUsers])
        except exceptions.NotFound:
            raise exceptions.NotFound("There are no users to view at the moment!")
        except:
            raise exceptions.InternalServerError()

@main.route('/users/<int:user_id>', methods=['GET', 'DELETE'])
def handleUserById(user_id):
    if request.method == 'GET':
        try: 
            user = Users.query.get_or_404(user_id)
            return  jsonify([user.serialize()])
        except exceptions.NotFound:
            raise exceptions.NotFound("User not found!")
        except:
            raise exceptions.InternalServerError()
    if request.method == 'DELETE':
        try: 
            user = Users.query.get_or_404(user_id)
            Users.remove(user)
            return f"User was sucessfully deleted!", 204
        except exceptions.NotFound:
            raise exceptions.NotFound("User not found!")
        except:
            raise exceptions.InternalServerError()

