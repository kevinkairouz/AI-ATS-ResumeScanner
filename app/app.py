from flask import Flask, jsonify  
from model import


app = Flask(__name__) 

@app.route("/parse") 
def parse(): 
    return ""