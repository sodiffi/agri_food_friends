import mysql.connector
from mysql.connector import Error


class DB():
    @property
    def select(self):
        return 0

    @property
    def create(self):
        return 1

    @property
    def update(self):
        return 2

    @property
    def delete(self):
        return 3

    __host = 'remotemysql.com'
    __user = 'YqwzgfQLW3'
    __dbname = 'YqwzgfQLW3'
    __password = 'KJBLXilYZ7'
    __conn = None

    @staticmethod
    def execution(type, sqlstr):
        try:
            connection = mysql.connector.connect(
                host=DB.__host,
                database=DB.__dbname,
                user=DB.__user,
                password=DB.__password,
                charset="utf8")
            if connection.is_connected():
                # 顯示資料庫版本
                # db_Info = connection.get_server_info()
                # print("資料庫版本：", db_Info)
                # 執行傳入的sql 指令
                cursor = connection.cursor(dictionary=True)
                if(isinstance(sqlstr, list)):
                    result = []
                    for sqlstrItem in sqlstr:                        
                        cursor.execute(sqlstrItem["sql"])
                        rows = cursor.fetchall()
                        result.append(
                            {"name": sqlstrItem["name"], "data": rows})
                    return {"success": True, "data": result}
                else:
                    if(type == DB.create or type == DB.update):
                        cursor.execute(sqlstr)
                        connection.commit()
                        return {"success": True}
                    else:
                        print(sqlstr)
                        cursor.execute(sqlstr)
                        rows = cursor.fetchall()
                        return {"success": True, "data": rows}

                cursor.close()
                connection.close()
                print("enter close")

        except Error as e:
            print("資料庫連接失敗：", e)
            cursor.close()
            connection.close()
            return {"success": False, "data": e}
