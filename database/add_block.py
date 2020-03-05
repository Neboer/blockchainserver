# 配合record，做底层操作，完成对数据库记录的增加。
def write_many(record_list, cursor, database):
    for record in record_list:
        cursor.execute("INSERT INTO test.datarecord(device_id,create_time,data_content,hash,prev_hash) values "
                       "(%s, %s, %s, (sha1(concat(device_id,create_time,data_content))), "
                       "(sha1(concat(hash,(SELECT prev_hash from datarecord order by id desc limit 1)))))",
                       (record.device_id, record.create_time, record.data,))
        database.commit()