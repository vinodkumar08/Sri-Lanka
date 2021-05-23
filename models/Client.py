from main import db

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String(225), unique=False, nullable=True)
    first_name = db.Column(db.String(225), unique=False, nullable=True)
    last_name = db.Column(db.String(225), unique=False, nullable=True)
    marital_status = db.Column(db.String(225), unique=False, nullable=True)
    occupation = db.Column(db.String(225), unique=False, nullable=True)
    address = db.Column(db.String(225), unique=False, nullable=True)
    city = db.Column(db.String(225), unique=False, nullable=True)
    state = db.Column(db.String(225), unique=False, nullable=True)
    zip_code = db.Column(db.Integer)
    phone_number = db.Column(db.String(225), unique=False, nullable=True)
    email = db.Column(db.String(225), unique=False, nullable=True)