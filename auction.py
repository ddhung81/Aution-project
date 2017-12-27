from flask import Flask,render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,ForeignKey

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

class Items(db.Model):
    __tablename__ = 'Items'
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(Integer, db.ForeignKey('Users.id'), nullable=False)
    ItemsBids = db.relationship('Bid', backref='Items', lazy=True)

    def __init__(self,id,name, description, start_date):
        self.id =id
        self.name = name
        self.description = description
        self.start_date = start_date

class Users(db.Model):
    __tablename__ = 'Users'
    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    Sales = db.relationship('Items', backref='Users', lazy=True)
    places_bid = db.relationship('Bid', backref='Users', lazy=True)

    def __init__(self,id,name,password):
        self.id =id
        self.name = name
        self.password = password

class Bid(db.Model):
    __tablename__ = 'Bid'
    id =Column(Integer,primary_key=True)
    float_price = Column(Integer)
    items_id = db.Column(db.Integer, db.ForeignKey('Items.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    def __init__(self, id, float_price):
        self.id = id
        self.float_price = float_price

@app.route('/insert')
def insert(Users):
    Users = Users('01','Duong','123456')
    Users = Users('01', 'Duong Duc', '123456')
    Users = Users('01', 'Duong Duc Hung', '123456')
    db.session.add(Users)
    db.session.commit()
    return "Inserted"
@app.route('/')
def hello_world():

    db.create_all()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,port=8899)
