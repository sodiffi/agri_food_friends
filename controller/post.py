from flask import Blueprint, request, Response
from model import postModel
import json
from coder import MyEncoder
from flask import app
from .util import ret
from datetime import datetime,timezone,timedelta
dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
dt2 = dt1.astimezone(timezone(timedelta(hours=8))) 
# 轉換時區 -> 東八區

print('UTC \t%s\nUTC+8\t%s'%(dt1,dt2))
print(dt2.strftime("%Y-%m-%d %H:%M:%S")) 
# 將時間轉換為 string

postEdit = Blueprint("post", __name__, url_prefix="/post")

@postEdit.route("/po", methods=["POST"])
def po():
    content = request.json
    arid= content['article_id']
    title = content['title']
    time = content['creat_time']
    content = content["content"]
    account = content['account']
    time
    data = postModel.edit(title, content,account)
    result = {"sucess": False, "data": data}


@postEdit.route("/poUpdate", methods=["PUT"])
def poUpdate():
    content = request.json
    title = content['title']
    content = content["content"]
    account = content['account']
    data = postModel.edit(title, content,account)
    result = {"sucess": False, "data": data}


'''@postEdit.route("/uploadPhoto", methods=["POST"])
def uploadPhoto():
    content = request.json'''


