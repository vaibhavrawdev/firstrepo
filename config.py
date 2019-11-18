import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
      SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
      MONGO_URI = os.environ.get('mongodb://localhost:27017')