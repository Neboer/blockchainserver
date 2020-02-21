from peewee import *


# internal method
def getDataBase(mysql_obj):
    mysql_db = MySQLDatabase(mysql_obj["db_name"], user=mysql_obj["username"], password=mysql_obj["password"],
                             host=mysql_obj["addr"], port=mysql_obj["port"])

    class BaseModel(Model):
        class Meta:
            database = mysql_db

    class DataRecord(BaseModel):
        device_id = IntegerField(primary_key=True)
        create_time = DateTimeField()
        data_content = CharField()

    return mysql_db, DataRecord
