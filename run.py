from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:1234@localhost:5432/archlimpa'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=False)
session = scoped_session(
    sessionmaker(bind=engine, autocommit=False, autoflush=False)
)

Base = declarative_base()

## Imports Controller Area
from app.Controller.UsuarioController import *
from app.Controller.LojistaController import *


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)  # type: ignore