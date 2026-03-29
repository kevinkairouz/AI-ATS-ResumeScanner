from model.category import Applicant
from google.cloud import bigquery 
from flask import Flask, Blueprint 
from flask_cors import CORS, cross_origin 


db = Blueprint("db")