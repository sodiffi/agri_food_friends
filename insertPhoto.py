#功能：將圖片匯入到MySQL資料庫
import sys
import mysql.connector
from mysql.connector import Error
from PIL import Image
import os

path = "C:\\Users\\agriphoto\\pro5.png"

# 讀取圖片檔案
fp = open("C:\\Users\\agriphoto\\pro5.png", 'rb')
img = fp.read()
path = 'C:\\Users\\Chihyu\\Desktop\\output.txt'
f = open(path, 'w')
f.write(str(img))
f.close()
fp.close()

# 建立一個MySQL連線
database = mysql.connector.connect(host="remotemysql.com", user="YqwzgfQLW3", passwd="KJBLXilYZ7", db="YqwzgfQLW3")
# 存入圖片
# 建立遊標
cursor = database.cursor()
# 注意使用Binary()函式來指定儲存的是二進位制
'''sql = "INSERT INTO pfpic VALUES  (%s, %s);"
args = ('05', img)
cursor.execute(sql, args)

database.commit()
# 關閉遊標
cursor.close()
# 關閉資料庫連線
database.close()
print("============")
print("Done! ")'''

