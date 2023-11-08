from flask import Blueprint, request, Response
from model import postModel
import json
from coder import MyEncoder
from flask import app
from .util import ret, checkParm,quickRet,get_next_id
from datetime import datetime, timezone, timedelta


postEdit = Blueprint("post", __name__, url_prefix="/post")
thumb = Blueprint("like", __name__, url_prefix="/like")


@postEdit.route("/", methods=["POST"])
def po():
    content = request.json
    cond = ["title", "content", "user_id",'create_time']
    check = checkParm(cond, request.json)
    result = {"success": False, "mes": "新增失敗"}
    check['id']=get_next_id("post")
    if isinstance(check, dict):
        check['content']=str(check["content"]).replace("\\n", "\n")
        result["mes"] = "新增異常"
        insert_result = postModel.po(check)
        print(insert_result.inserted_id)
        if insert_result.inserted_id:
            # result['data']=data
            result["success"] = True
            result["mes"] = "新增成功"
    
    return ret(result)


@postEdit.route("/", methods=["PUT"])
def poUpdate():
    content = request.json
    title = content["title"]
    content = content["content"]
    account = content["account"]
    data = postModel.edit(title, content, account)
    result = {"sucess": False, "data": data}
    return ret(data)


@postEdit.route("/", methods=["GET"])
def show():
    return quickRet(postModel.show())


@postEdit.route("/mes", methods=["POST"])
def mes():
    content = request.json
    article_id = content["article_id"]
    user_id = content["user_id"]
    con = content["content"]

    data = postModel.message(article_id, user_id, con)
    return ret(data)


@thumb.route("/", methods=["POST"])
def clickLike():
    content = request.json
    message_id = content["message_id"]
    account = content["account"]
    data = postModel.like(message_id, account)
    result = {"sucess": False, "data": data}
    return ret(data)


"""@postEdit.route("/uploadPhoto", methods=["POST"])
def uploadPhoto():
    content = request.json"""
