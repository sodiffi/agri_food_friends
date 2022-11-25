from model.db import DB
import json

from model.util import group_msg

def po(title,content,account):
    print("this is po")
    sqlstr = "insert into article(title,content,account) VALUES (\"%s\",\'%s\',\"%s\")" % (
         title,content,account)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)


def edit(title,content,account):
    sqlstr = "update article set title = \"%s\" and content = \"%s\" where account = \"%s\"" % (
        title, content, account)
    return DB.execution(DB.update, sqlstr)


def show():
    sqlstr = 'select article.title,article.account,article.creat_time,article.content,article.article_id,message.content  as m_c ,message.user_id  ,message.time  from article  left outer join message on article.article_id = message.article_id;'
    data=DB.execution(DB.select, sqlstr)
    
    return group_msg(data['data'],["m_c","user_id","time"],"article_id")

def like(message_id,account):
    sqlstr ="insert into like(message_id,account) VALUES (\"%s\",\"%s\")" % (
         message_id,account)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)

def message(article_id,user_id,content):
    sqlstr = "insert into message(article_id,user_id,content) VALUES(\"%s\",\"%s\",\"%s\")" %(
        article_id,user_id, content)
    print(sqlstr)
    return DB.execution(DB.create ,sqlstr)

