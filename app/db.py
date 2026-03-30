from model.category import Applicant
from google.cloud import bigquery 
from flask import Flask, Blueprint 
from flask_cors import CORS, cross_origin 


db = Blueprint("db", __name__) 


db.route("/sendInfo", methods = ["POST"]) 
def sendInfo(): 
    query = "insert into resumeSystem.applicants values ()"
    #this will send data to BigQuery

    return None