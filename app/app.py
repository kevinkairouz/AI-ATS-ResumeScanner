from flask import Flask, jsonify  
from model.resume import ResumeManager 
from model.category import CategoryManager 
from model.role import TechRoleManager 
from model.score import 


app = Flask(__name__) 

@app.route("/parse") 
def parse(): 
    return ""