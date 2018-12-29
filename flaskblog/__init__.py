from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '3638836a16e1e56ee58871cfaf32e290'

# configure the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask-blog'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# instatiate an object for SQLAlchemy module .
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

#import the routes
from flaskblog import routes
