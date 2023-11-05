from model.sqldb import DB
import json


def login(account, password):
    pass
    # sqlstr = "select * from user where account=\"%s\" and password = \"%s\"" % (
    #     account, password)
    # return (DB.execution(DB.select, sqlstr))


def findPasswordByAccount(account):
    pass
    # sqlstr = "select password from user where account=\"%s\"" % account
    # return DB.execution(DB.select, sqlstr)


def changePassword(account, password):
    pass
    # sqlstr = "update user set password = \"%s\" where account = \"%s\"" % (
    #     password, account)
    # return DB.execution(DB.update, sqlstr)


def sign(account, password, area_id, name,usertype_id):
    pass
    # sqlstr = "insert into user(account, password,area_id,name,usertype_id) VALUES (\"%s\", \"%s\" ,\"%s\",\"%s\",\"%s\")" % (
    #      account, password, area_id, name,usertype_id)
    # print(sqlstr)
    # return DB.execution(DB.create, sqlstr)


def changeProfile(data, account):
    pass
    # strCond = ""
    # if(isinstance(data, dict)):
    #     for i in data.keys():
    #         strCond += " %s = \"%s\" ," % (i, data[i])
    # sqlstr = "update user set %s where account=\"%s\"" % (
    #     strCond[0:len(strCond)-1], account)
    # print(sqlstr)
    # return DB.execution(DB.update, sqlstr)


def hasUser(userid):
    pass
    # sqlstr = "select count(*) from user where account=\"%s\"" % (userid)
    # return DB.execution(DB.select, sqlstr)

