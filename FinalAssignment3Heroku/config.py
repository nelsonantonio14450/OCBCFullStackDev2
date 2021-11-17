import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))


connex_app = connexion.App(__name__, specification_dir=basedir)


app = connex_app.app


app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://erygdlwbegzxbz:653a860f930fbf5c5ed31f00f775d8eb1d2dbf85286e145cfbe2e8149a0b62e1@ec2-44-199-158-170.compute-1.amazonaws.com:5432/dchhkdussk985b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


ma = Marshmallow(app)
