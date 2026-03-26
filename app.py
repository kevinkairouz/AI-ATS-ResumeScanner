from flask import Flask, jsonify, request
from model.resume import ResumeManager 
from model.category import CategoryManager 
from model.role import TechRoleManager 
from model.score import ScoreManager 
from model.other_role import NonTechRoleManager

        
app = Flask(__name__)  

def predict(resume):  
    rmanager = ResumeManager() 
    cmanager = CategoryManager() 
    tmanager = TechRoleManager() 
    smanager = ScoreManager() 
    omanager = NonTechRoleManager() 

    #TODO include score and nontechroleManager we may changed ScoreManagerNonTech 

    text = rmanager.getText(resume)  
    classification = cmanager.makePrediction(text) 
    if classification == "INFORMATION-TECHNOLOGY" or classification == "BUSINESS" or classification == "ENGINEERING": 
        role = tmanager.predictRole(text) 
        return role        
    else:

        return classification
    
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
            return "No file yet"

@app.route("/uploadResumes", methods = ["POST"]) 
def uploadResumes(): 
    files = request.args.getlist("file") 
    roles = [] 
    for file in files: 
        role = predict(file) 
        roles.append(role) 
    return jsonify({"ROLES": roles})
        
        
app.run()


