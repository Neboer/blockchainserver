class RecordBlock:  # 用于被调用接收客户端发来的信息,测试hash是否正确，存入数据库
    def __init__(self, device_id, create_time, data_content):
        self.device_id = device_id,
        self.create_time = create_time,
        self.data_content = data_content

    def hash_test(self):
        return 0;  # 写不动了，下次再来
