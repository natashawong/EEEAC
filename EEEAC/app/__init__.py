from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'peanutbutter'
app.static_folder = 'static'

from app import routes

bootstrap = Bootstrap(app)
