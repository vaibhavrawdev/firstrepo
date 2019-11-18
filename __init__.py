from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__,)
app.config.from_object(Config)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
#breakpoint()

from app import routes
