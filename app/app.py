from flask import Flask, jsonify, request, blueprints, Blueprint 
from flask_cors import CORS, cross_origin
from model.resume import ResumeManager 
from model.category import CategoryManager  
from dataclasses import dataclass 


# @dataclass
# class Record: #this is the record that we are sending to bigQuery
#     first_name: str 
#     last_name: str 
#     primary_role: str 
#     secondary_role: str 
#     role_applied: str

  




app = Flask(__name__) 
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
        #then get the first_name and last_name and the primrary_role turn that into a record 
        # make the object and return it to frontend bc the job portal wont use what is returned
        # from function but web application will use it percisley the first_name, last_name and the roles 
         
        return True

        

@app.route("/display", methods = ["POST"]) 
def display():
    #TODO: will be same as uplaod however it is geared towards returning data 
    # to frontend instead of sending data to PROJXON 
     
    return "" 



