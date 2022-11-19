from model.db import DB
import json

#爬蟲
#新增活動
def insertCam(cam_id,name,start_time,end_time,location,content,charge_ppl,charge_phone,source):
    sqlstr = "insert into campaign(cam_id,name,start_time,end_time,location,content,charge_ppl,charge_phone,source) VALUES (\"%s\", \"%s\" ,\"%s\",\"%s\",\"%s\", \"%s\" ,\"%s\",\"%s\",\"%s\")" % (
         cam_id,name,start_time,end_time,location,content,charge_ppl,charge_phone,source)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)
