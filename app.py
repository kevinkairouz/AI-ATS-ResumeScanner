from flask import Flask, jsonify, request, flash
from model.resume import ResumeManager 
from model.category import CategoryManager 
from model.role import TechRoleManager 
from model.score import ScoreManager


app = Flask(__name__)  

allowed_extensions = {"pdf"}

def predict(resume): 
    #This will be a helper funtion so we can loop through
    #the resumes and call this function everytime 
    rmanager = ResumeManager() 
    text = rmanager.getText(resume) 
      
    return "None"

@app.route("/") 
def greet(): 
    return "Hello There!!" 


@app.route("/uploadResume", methods = ["POST"]) 
def upload(): 
    file = request.args.getlist("file") 
    if file.filename == "": 
        flash("ERROR: NO FILE SELECTED") 
    else: 




