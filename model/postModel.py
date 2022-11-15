from model.db import DB
import json

def post(article_id,title,content,account):
    sqlstr = "insert into article(article_id,title,content,account) VALUES (\"%s\", \"%s\" ,\"%s\",\"%s\")" % (
         article_id,title,content,account)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)

