import MySQLdb


def connect(mysql_config):
    database = MySQLdb.connect(host=mysql_config.host, user=mysql_config.username, passwd=mysql_config.password)
    database.select_db(mysql_config.database)
    cur = database.cursor()
    return database, cur
