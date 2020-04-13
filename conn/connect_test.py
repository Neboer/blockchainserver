from conn import connection


db = connection.connect()
cursor = db.cursor()
sql = "select * from users;"
cursor.execute(sql)
res = cursor.fetchone()
print(res)