from sqlalchemy import Column, String, create_engine, Integer
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['DATABASE_URL']

# database_name = "alo"
# database_path = "postgres://{}:{}@{}/{}".format('alo', '1234', 'localhost:5432', database_name)


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):  
    __tablename__ = 'People'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    catchphrase = Column(String)
    bober = Column(Integer)

    def __init__(self, name, catchphrase=""):
      self.name = name
      self.catchphrase = catchphrase

    def format(self):
      return {
        'id': self.id,
        'name': self.name,
        'catchphrase': self.catchphrase}