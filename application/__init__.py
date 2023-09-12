from flask import Flask, session
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'key'


db.init_app(app)


import application.routes