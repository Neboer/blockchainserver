# Record类是一个记录的抽象内容。这个类具有如下特征：
# 自创建之后，类的实例对象保存在内存，在收到“共识”请求后把数据统一编码发往 服务器。

class Record():
    def __init__(self, serial_number, device_id, create_time, data):
        # create_time是unix-timestamp的形式，应该是一个四位小数的浮点数。
        self.serial_number = serial_number
        self.device_id = device_id
        self.create_time = create_time
        self.data = data

    # 序列化数据内容，便于发送。数据在发送的过程中应该有签名+校验的问题
    def serialize(self):
        return str(self.serial_number) + self.device_id + str(self.create_time) + self.data
