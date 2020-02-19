from peewee import *


# internal method
def connect_to_db(mysql_obj):
    mysql_db = MySQLDatabase(mysql_obj["db_name"], user=mysql_obj["username"], password=mysql_obj["password"],
                             host=mysql_obj["addr"], port=mysql_obj["port"])
    return mysql_db


def init_table(mysql_obj):
    conn_database = connect_to_db(mysql_obj)

    class BaseModel(Model):
        class Meta:
            database = conn_database

    return BaseModel


def data_record_table(BaseModel):
    class DataRecord(BaseModel):
        device_id = IntegerField(primary_key=True)
        create_time = DateTimeField()
        data_content = CharField()

    return
