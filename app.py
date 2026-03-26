from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from model.resume import ResumeManager 
from model.category import CategoryManager 
from model.role import TechRoleManager 
from model.score import ScoreManager 
from model.other_role import NonTechRoleManager 
import mysql.connector as sql


        
app = Flask(__name__)   
CORS(app, resources={r"/api/*": {"origins": "*"}})
r_m = ResumeManager()

def predict(resume):  
    r = ResumeManager() 
    c = CategoryManager() 
    t = TechRoleManager() 
    s = ScoreManager() 
    o = NonTechRoleManager()  
    tech_roles = ["BUSINESS","ENGINEERING","FINANCE","INFORMATION-TECHNOLOGY"]



    #TODO include score and nontechroleManager we may changed ScoreManagerNonTech 

    text = r.getText(resume)  
    classification = c.makePrediction(text) 
    message = send_data(text, classification)
    if classification in tech_roles: 
        projxon_role = t.predictRole(text) 
        return s.isFit(text,projxon_role)
    else:  
        return o.is_Fit(text, classification) 
    

def send_data(resume, classification): 
    inserted_data = (resume, classification)
    db = sql.connect(root = "user", password = "Dominics1", host = "localhost", database = "resumes") 
    cursor = db.cursor() 
    cursor.execute("insert into applicants values (%s, %s)")
    db.commit() 
    return "COMPLETED DB TRANSACTION"

@app.route("/") 
@cross_origin()
def greet(): 
    return "Hello There!!" 

@app.route("/uploadResume", methods = ["POST"]) 
@cross_origin()
def upload():          
        if "file" in request.files: 
            pdf = request.files["file"] 
            if pdf.filename == "" or r_m.getText(pdf) == "": 
                return "JUNK FILE"
            else:       
                res = predict(pdf) 
                return jsonify({"ROLE": res}) 
        else: 
            return "No file yet"

app.run(debug=True)
#V1 will not include a list of resumes TBD feature
# @app.route("/uploadResumes", methods = ["POST"])
# @cross_origin()
# def uploadResumes(): 
#     files = request.args.getlist("file") 
#     roles = [] 
#     for file in files: 
#         role = predict(file) 
#         roles.append(role) 
#     return jsonify({"ROLES": roles})
        
        
# app.run()


