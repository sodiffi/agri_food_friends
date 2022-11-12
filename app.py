from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>食農好朋友test two</p>"
