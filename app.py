# app.py
import os
from flask import Flask, Response, request, abort
from coder import MyEncoder
from model.db import mongo
import json
import sys
# from model.line import lineModule
from controller import(user,post,event)

#  ----------------------- 

from flask_cors import CORS


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://numbone112:i3PO8xrZj1KRwz83@cluster0.5rqnhen.mongodb.net/argi_food"
mongo.init_app(app) # initialize here!
print(type(mongo))
print((mongo.db.name))
app.register_blueprint(user.userProfile)
app.register_blueprint(post.postEdit)
#  ----------------------- 

# CORS(app)


@app.route('/', methods=["POST"])
def line():
    return "ok"


@app.route('/get', methods=["GET","OPTIONS"])
def home():
    return 'good from backend'