from flask import Flask, request, jsonify, blueprints, Blueprint
from app.db import db
application = Flask(__name__)  

