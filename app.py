import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# migrate = Migrate(app, db)

from models import Users, Products, Category

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/products', methods=['GET','POST'])
def gatAllProducts():
    if request.method == 'GET':
        try: 
            allProducts = Products.query.all()
            return  jsonify([e.serialize() for e in allProducts])
        except exceptions.NotFound:
            raise exceptions.NotFound("There are no products to view at the moment!")
        except:
            raise exceptions.InternalServerError()

    elif request.method == 'POST':
    # format of request { description, category_id, is_retail, location, price, expiry, image} 
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

@app.get('/products/<int:product_id>')
def getProductById(product_id):
    try: 
        product = Products.query.get_or_404(product_id)
        return  jsonify([product.serialize()])
    except exceptions.NotFound:
        raise exceptions.NotFound("Product not found!")
    except:
        raise exceptions.InternalServerError()



if __name__ == '__main__':
    app.run(debug=True)
