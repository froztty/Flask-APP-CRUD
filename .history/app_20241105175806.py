from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def index():
    