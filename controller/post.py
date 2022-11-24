from flask import Blueprint, request, Response
from model import postModel
import json
from coder import MyEncoder
from flask import app
from .util import ret
from datetime import datetime,timezone,timedelta


postEdit = Blueprint("post", __name__, url_prefix="/post")
thumb = Blueprint("like", __name__, url_prefix="/like")


@postEdit.route("/", methods=["POST"])
def po():
    print(request.headers)
    print(request.is_json)
    print(request.get_json())

    content = request.json

    title = content['title']
    con = content['content']
    account = content['account']
    data = postModel.po(title,con,account)
    print(data)
    result = {"sucess": False, "message":"新增異常","data": data}
    if(data["success"]):
        result["success"] = True
        result["message"] = "新增成功"
    else:
        result["message"] = "新增失敗"

    return ret(data)

@postEdit.route("/", methods=["PUT"])
def poUpdate():
    content = request.json
    title = content['title']
    content = content["content"]
    account = content['account']
    data = postModel.edit(title, content,account)
    result = {"sucess": False, "data": data}
    return ret(data)


@postEdit.route("/",methods=["GET"])
def show():
    print("here")
    d=postModel.show()
    return ret(d)

@postEdit.route("/mes", methods=["POST"])
def mes():
    content = request.json
    id = content['id']
    user_id = content['user_id']
    con = content['content']
    data = postModel.message(id,user_id,con)
    return ret(data)


@thumb.route("/", methods=["POST"])
def clickLike():
    content = request.json
    message_id = content["message_id"]
    account = content['account']
    data = postModel.like(message_id,account)
    result = {"sucess": False, "data": data}
    return ret(data)

'''@postEdit.route("/uploadPhoto", methods=["POST"])
def uploadPhoto():
    content = request.json'''


