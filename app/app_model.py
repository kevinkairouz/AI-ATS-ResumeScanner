from flask import Flask, jsonify, request, blueprints, Blueprint 
from flask_cors import CORS, cross_origin
from model.resume import ResumeManager 
from model.category import CategoryManager  
from dataclasses import dataclass 


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
    if pdf.filename == "": 
        return "ERROR, INVALID FILENAME" 
    else: 
        a = predict(pdf) 
        pfit = a[0]
        sfit = a[1] 
        return jsonify({"Primary Fit": pfit, "Secondary Fit": sfit}) 
         

#returning to the front end is the primary and the secondary fit for such candidate and we send it to the frontend 
