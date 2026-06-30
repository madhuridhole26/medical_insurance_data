from flask import Flask,jsonify,request,render_template
from flask_jwt_extended import JWTManager, create_access_token,jwt_required,get_jwt_identity,verify_jwt_in_request
import pandas as pd
import numpy as np
import pymongo
import config
from src.utils import MedicalInsurence
import datetime

medical_insurence_obj=MedicalInsurence()

app=Flask(__name__)
jwt=JWTManager(app)
app.config["JWT_SECRET_KEY"]="secret"
app.config["SECRET_KEY"]="flask-session-secret"
mongo_client=pymongo.MongoClient(config.MONGO_CLIENT)
db=mongo_client[config.mongo_db]
collection_user=db["user_collection_name"]

@app.route("/")
def home():
    return render_template("kaps.html")

@app.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    user_data=request.form
    user_name=user_data['user_name']
    password=user_data["password"]
    email_id=user_data["email_id"]
    Contact_no=user_data["contact_no"]
    dob=user_data["dob"]
    response=collection_user.find_one({"user_name":user_name,"password":password})
    if not response:
        collection_user.insert_one({"user_name":user_name,"password":password,"email_id":email_id,"contact_no":Contact_no,"dob":dob})
        return jsonify({"message":"user registered successfully"})
    else:
        return jsonify({"message":"user already exists"})

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    user_data=request.form
    user_name=user_data["user_name"]
    password=user_data["password"]
    response=collection_user.find_one({"user_name":user_name,"password":password})
    if response:
        access_token=create_access_token(identity=user_name,expires_delta=datetime.timedelta(minutes=2))
        return jsonify({"Access_token":access_token,"status":"Success","message":"login successful"})
    else:
        return jsonify({"status":"Failure","message":"invalid credentials"})

@app.route("/predict", methods=["GET"])
def predict_page():
    return render_template("predict.html")

@app.route("/predict", methods=["POST"])
@jwt_required()
def predict():
    user_data=request.form
    prediction=medical_insurence_obj.predict_charges(user_data)
    return jsonify({"predicted_charges":prediction})

if __name__=="__main__":
    app.run(host=config.FLASK_HOST,port=config.FLASK_PORT,debug=True)
