from app import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(100))
    password = db.Column(db.String(25))
    rating = db.Column(db.Float)
    rating_num = db.Column(db.Integer)
    location = db.Column(db.String(7))
    radius = db.Column(db.Float)

    def __init__(self, username, email, password, rating, rating_num, location, radius):
        self.username = username
        self.email = email
        self.password = password
        self.rating = rating
        self.rating_num = rating_num
        self.location = location
        self.radius = radius
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username, 
            'email': self.email,
            'password': self.password,
            'rating': self.rating,
            'rating_num': self.rating_num,
            'location': self.location,
            'radius': self.radius
    }


class Products(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    is_retail = db.Column(db.Boolean)
    location = db.Column(db.String(7))
    price = db.Column(db.Float)
    expiry = db.Column(db.String(15))
    description = db.Column(db.String(100))
    image = db.Column(db.String(500))

    def __init__(self, user_id, category_id, is_retail, location, price, expiry, description, image):
        self.user_id = user_id
        self.category_id = category_id
        self.is_retail = is_retail
        self.location = location
        self.price = price
        self.expiry = expiry
        self.description = description
        self.image = image

    def __repr__(self):
        return '<id {}>'.format(self.product_id)
    
    def serialize(self):
        return {
            'product_id': self.product_id,
            'user_id': self.user_id, 
            'category_id': self.category_id,
            'is_retail': self.is_retail,
            'location': self.location,
            'price': self.price,
            'expiry': self.expiry,
            'description': self.description,
            'image': self.image
    }


class Categories(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True)
    category_name  = db.Column(db.String(100))

    def __init__(self, category_name):
        self.category_name = category_name

    def __repr__(self):
        return '<id {}>'.format(self.category_id)
    
    def serialize(self):
        return {
            'category_id': self.category_id, 
            'category_name': self.category_name
        }