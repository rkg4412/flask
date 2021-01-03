from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import create_engine
app = Flask(__name__)
login=LoginManager(app)
bcrpyt=Bcrypt(app)
db=SQLAlchemy(app)
login.login_view='login_form'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:roottiger@localhost/flaskdb'
app.config['SECRET_KEY']='779a53f26fd53494bf728561ad371a3e'



from lab import routes