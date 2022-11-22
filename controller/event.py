from flask import Blueprint, request, Response
from model import eventModel
import json
from coder import MyEncoder
from flask import app
from .util import ret

eventRec = Blueprint("event", __name__, url_prefix="/event")

@eventRec.route("/", methods=["POST"])
def eventInsert():
    content = request.json
    name = content['name']
    start_time = content["start_time"]
    end_time = content['end_time']
    location = content['location']
    content = content['content'] #欄位改名
    charge_ppl = content['charge_ppl']
    charge_phone = content['charge_phone']
    source = content['source']
    data = eventModel.edit()
    result = {"sucess": False, "data": data}


@eventRec.route("/", methods=["GET"])
def searchEve():
    content = request.json
    name = content["name"]
    data = eventModel.findUserarea(name)
    return Response(json.dumps(data, cls=MyEncoder), mimetype="application/json")

