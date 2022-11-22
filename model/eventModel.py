from model.db import DB
import json

def insert(name,start_time,end_time,location,content,charge_ppl,charge_phone,source):
    print("this is po")
    sqlstr = "insert into event(name,start_time,end_time,location,content,charge_ppl,charge_phone,source) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (
         name,start_time,end_time,location,content,charge_ppl,charge_phone,source)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)

def show():
    sqlstr = "select * from event"
    print(sqlstr)
    return DB.execution(DB.select, sqlstr)