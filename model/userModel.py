from model.db import DB
import json


def login(account, password):
    sqlstr = "select * from user where account=\"%s\" and password = md5(\"%s\")" % (
        account, password)
    return (DB.execution(DB.select, sqlstr))


def findPasswordByAccount(account):
    sqlstr = "select password from user where account=\"%s\"" % account
    return DB.execution(DB.select, sqlstr)


def changePassword(account, password):
    sqlstr = "update user set password = \"%s\" where account = \"%s\"" % (
        password, account)
    return DB.execution(DB.update, sqlstr)

# 待修
# def sign(account, password, age, sex, area, name):
    # sqlstr = "insert into user(account, password,age,gender,area_id,name) VALUES (\"%s\", \"%s\" ,\"%s\" ,\"%s\",\"%s\",\"%s\")" % (
    #     account, password, age, sex, area, name)
    # print(sqlstr)
    # return DB.execution(DB.create, sqlstr)


def changeProfile(data, account):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" ," % (i, data[i])
    sqlstr = "update user set %s where account=\"%s\"" % (
        strCond[0:len(strCond)-1], account)
    print(sqlstr)
    return DB.execution(DB.update, sqlstr)


def hasUser(userid):
    sqlstr = "select count(*) from user where account=\"%s\"" % (userid)
    return DB.execution(DB.select, sqlstr)

