from flask import Flask,blueprints, Blueprint
from app.db import db 
from app.app_model import app_model



application = Flask(__name__)     
application.register_blueprint(db, url_prefix = "/data") 
application.register_blueprint(app_model, url_prefix = "/model") 
application.run(debug=True)