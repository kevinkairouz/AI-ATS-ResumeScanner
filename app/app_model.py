from flask import Flask, jsonify, request, blueprints, Blueprint 
from flask_cors import CORS, cross_origin
from model.resume import ResumeManager 
from model.category import CategoryManager  
from dataclasses import dataclass 
import app.db as d 


app = Flask(__name__) 
CORS(app)  
app_model = Blueprint("app_model", __name__)



def predict(resume): 
    r = ResumeManager() 
    c = CategoryManager()  
    resume_txt = r.getText(resume) 
    applicant = c.makePrediction(resume_txt) 
    return applicant 
    

@app_model.route("/") 
@cross_origin()
def greet(): 
    return "Hello There!!" 

@app_model.route("/uploadResume", methods = ["POST"]) 
@cross_origin()
def upload():
    pdf = request.files["file"] 
    data = request.json() 
    first_name = data["first_name"] 
    last_name = data["last_name"] 
    email = data["email"]
    role_applied = data["role_applied"]

    if pdf.filename == "": 
        return "ERROR, INVALID FILENAME" 
    else: 
        a = predict(pdf) 
        pfit = a[0]
        sfit = a[1] 
        return d.send_data(first_name, last_name, pfit, sfit, role_applied) 
         


        #then get the first_name and last_name and the primrary_role turn that into a record 
        # make the object and return it to frontend bc the job portal wont use what is returned
        # from function but web application will use it percisley the first_name, last_name and the roles 
      

