from peewee import *


# internal method
def getDataBase(mysql_obj):
    mysql_db = MySQLDatabase(mysql_obj["db_name"], user=mysql_obj["username"], password=mysql_obj["password"],
                             host=mysql_obj["addr"], port=mysql_obj["port"])

    class BaseModel(Model):
        class Meta:
            database = mysql_db

    class Users(BaseModel):  # 用户表
        device_id = IntegerField(primary_key=True)
        username = CharField()  # 用户名
        password = CharField()

    class DataRecord(BaseModel):
        device_id = IntegerField()  # 设为参照用户表的外键 ps:这个外键把爷给整懵了，你来整下吧
        create_time = DateTimeField(primary_key=True)
        data_content = CharField()
        previous_hash = CharField()  # 前一列的hash值
        hash = CharField()  # 当前列表的hash

    return mysql_db, Users, DataRecord
