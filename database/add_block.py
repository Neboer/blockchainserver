# 配合record，做底层操作，完成对数据库记录的增加。
def write_many(record_list, cursor, database):
    for record in record_list:
        cursor.execute("INSERT INTO blocks (device_id, create_time, data_content) values (%s, %s, %s)",
                       (record.device_id, record.create_time, record.data))
    database.commit()
    cursor.execute("CALL wrapped_insert()")
    database.commit()
