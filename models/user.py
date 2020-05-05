from conn.connection import connect


class User:
    def __init__(self, device_id):
        self.device_id = device_id
        self.user_name = False
        self.user_password = 1
        if self.get_user():
            self.user_name = self.get_user()[0]
            self.user_password = self.get_user()[1]

    def get_user(self):
        try:
            db = connect()
            cursor = db.cursor()
            sql = "select * from users where device_id = %s"
            cursor.execute(sql, self.device_id)
            res = cursor.fetchone()
            return res
        except:
            return False
