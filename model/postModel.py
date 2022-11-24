from model.db import DB
import json

from model.util import group_msg

def po(title,content,account,creat_time):
    print("this is po")
    sqlstr = "insert into article(title,content,account,select creat_time,convert_tz(creat_time,'+00:00','+08:00')) VALUES (\"%s\",\"%s\",\"%s\",\"%s\")" % (
         title,content,account,creat_time)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)


def edit(title,content,account):
    sqlstr = "update article set title = \"%s\" and content = \"%s\" where account = \"%s\"" % (
        title, content, account)
    return DB.execution(DB.update, sqlstr)


def show():
    sqlstr = "select article.title,article.acc,article.content,article.article_id,message.content as m_c ,message.user_id from article  left join message on article.article_id = message.article_id;"
    data=DB.execution(DB.select, sqlstr)
    return group_msg(data['data'],["m_c","user_id"],"article_id")

def like(message_id,account):
    sqlstr ="insert into like(message_id,account) VALUES (\"%s\",\"%s\")" % (
         message_id,account)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)

def message(id,user_id,content):
    sqlstr = "insert into message(id,user_id,content) VALUES(\"%s\",\"%s\",\"%s\")" %(
        id,user_id, content)
    print(sqlstr)
    return DB.execution(DB.create ,sqlstr)

