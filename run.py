from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:1234@localhost:5432/archlimpa'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.Controller.parentsController import *
from app.Model.FilhoTable import Filho
from app.Model.GenitorTable import Genitor

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="5000", debug=True)
