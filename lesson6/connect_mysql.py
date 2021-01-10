import pymysql

'''面试常问的python连数据库操作'''
# 连接数据库
db = pymysql.connect(host="49.235.92.12",
                     port=3309,
                     user='root',
                     password='123456',
                     database='apps',
                     cursorclass=pymysql.cursors.DictCursor)
# 创建游标
cursor = db.cursor()

# sql = "SELECT * FROM apiapp_userpersonalinfo;"
# cursor.execute(sql)
# results = cursor.fetchall()
# print(results) #tuple of tuple

sql = 'UPDATE apiapp_userpersonalinfo set age = 21 WHERE name="test";'
cursor.execute(sql)
db.commit()
db.close()