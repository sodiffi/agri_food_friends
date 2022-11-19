from model.db import DB
import json

#自動產生的artid需要寫入嗎?
def po(article_id,title,content,account):
    sqlstr = "insert into article(article_id,title,content,account) VALUES (\"%s\", \"%s\" ,\"%s\",\"%s\")" % (
         article_id,title,content,account)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)

'''def delPost(article_id,title,content,account):
    sqlstr = "delete * from article" % ()
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)'''
