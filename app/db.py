import os 
from model.category import Applicant
from google.cloud import bigquery 
from flask import Flask, Blueprint, request
from flask_cors import CORS, cross_origin   
import mysql.connector as sql

db = Blueprint("db", __name__)  
CORS(db)


@db.route("/sendInfo", methods = ["POST"])  
@cross_origin()
def sendInfo():   
    conn = sql.connect(host = "localhost", user = "root", password = "Dominics1", database = "projxon")
    data = request.json() 
    first_name = data["firstName"] 
    last_name = data["lastName"] 
    primary_role = data["primaryRole"] 
    secondary_role = data["secondaryRole"] 
    role_applied = data["roleApplied"] 

    insert_data = (first_name, last_name, primary_role, secondary_role, role_applied)  
    query = "insert into applicants values (%s,%s,%s,%s,%s)"  

    cur = conn.cursor()
    cur.execute(query, insert_data) 
    conn.commit() 
    """ 
    using mySQL until bigQuery works/is up and running
    """
    return "Success"


    


