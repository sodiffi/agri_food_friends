from flask import Blueprint, request, Response
from model import postModel
import json
from coder import MyEncoder
from flask import app
from .util import ret

postEdit = Blueprint("post", __name__, url_prefix="/post")

@postEdit.route("/po", methods=["POST"])
def po():
    content = request.json
    title = content['title']
    content = content["content"]
    account = content['account']
    data = postModel.edit(title, content,account)
    result = {"sucess": False, "data": data}