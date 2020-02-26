from tools import compute_md5


class RecordBlock:  # 用于被调用接收客户端发来的信息,测试hash是否正确，存入数据库
    def __init__(self, device_id, create_time, data_content, previous_hash):
        self.device_id = device_id
        self.create_time = create_time
        self.data_content = data_content
        self.previous_hash = previous_hash
        information = device_id + create_time + data_content + previous_hash
        self.hash = compute_md5(information)

    def hash_test(self):  # 检验当前区块是否符合符合条件
        information = self.device_id + self.create_time + self.data_content + self.previous_hash
        hash = compute_md5(information)
        c = 0
        if hash == self.hash:
            c = 1
        return c
