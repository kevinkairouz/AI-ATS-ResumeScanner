from flask import Flask, jsonify, request, blueprints, Blueprint 
from flask_cors import CORS, cross_origin
from model.resume import ResumeManager 
from model.category import CategoryManager  
from dataclasses import dataclass 


class Record: 
    data: str 
  




app = Flask(__name__) 
app.register_blueprint("")
CORS(app) 





def predict(resume): 
    r = ResumeManager() 
    c = CategoryManager()  
    resume_txt = r.getText(resume) 
    applicant = c.makePrediction(resume_txt) 
    return applicant 
    

@app.route("/") 
@cross_origin()
def greet(): 
    return "Hello There!!" 

@app.route("/uploadResume", methods = ["POST"]) 
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
        #TODO test with your resume and see where the fits are and determine from there watch the 
        #match rate % should be the and the logic for a candidate to show up on the sheet because all candidates
        #will appear in bigQuery for analytics/dashboard purpose 

        if role_applied == a.PrimaryFit: 
            return "y"
            #send to the sheet & db by using our Record Dataclass
        elif role_applied == a.Secondary1 and a.score2 > 22.0: 
            #send to the sheet & db by using our Record Dataclass
            return "k"
        elif role_applied == a.Secondary2 and a.score3 > 22.0: 
            return "k" 
        else: 
            return "CANDIDATE REJECTED"


app.run()


