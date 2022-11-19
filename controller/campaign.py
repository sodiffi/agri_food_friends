from flask import Blueprint, request, Response
from model import campaignModel
import json
from coder import MyEncoder
from flask import app
from .util import ret

campaignRec = Blueprint("campaign", __name__, url_prefix="/campaign")

@campaignRec.route("/insert", methods=["POST"])
def campaignInsert():
    content = request.json
    name = content['name']
    start_time = content["start_time"]
    end_time = content['end_time']
    location = content['location']
    content = content['content'] #欄位改名
    charge_ppl = content['charge_ppl']
    charge_phone = content['charge_phone']
    source = content['source']
    data = campaignModel.edit()
    result = {"sucess": False, "data": data}


@campaignRec.route("/search", methods=["GET"])
def searchCam():
    content = request.json
    name = content["name"]
    data = campaignModel.findUserarea(name)
    return Response(json.dumps(data, cls=MyEncoder), mimetype="application/json")

