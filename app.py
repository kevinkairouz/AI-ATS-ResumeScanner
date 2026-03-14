from flask import Flask, jsonify, request, flash
from model.resume import ResumeManager 
from model.category import CategoryManager 
from model.role import TechRoleManager 
from model.score import ScoreManager


app = Flask(__name__)  

def predict(resume):  
    rmanager = ResumeManager() 
    cmanager = CategoryManager() 
    tmanager = TechRoleManager() 
    smanager = ScoreManager() 

    text = rmanager.getText(resume)  
    classification = cmanager.makePrediction(text) 
    if classification[0] == "INFORMATION-TECHNOLOGY" or classification[0] == "BUSINESS" or classification[0] == ["ENGINEERING"]: 
        role = tmanager.predictRole(text) 
        return role        
    else:  
        return classification[0]
    
    
r_m = ResumeManager()


      

@app.route("/") 
def greet(): 
    return "Hello There!!" 


@app.route("/uploadResume", methods = ["POST"]) 
def upload(): 
        if "file" in request.files: 
            pdf = request.files["file"] 
            if pdf.filename == "" or r_m.getText(pdf) == "": 
                return "JUNK FILE"
            else:       
                role = predict(pdf) 
                return jsonify({"ROLE": role}) 
        else: 
            flash("ERROR: NO FILE ATTACHED")




app.run()


