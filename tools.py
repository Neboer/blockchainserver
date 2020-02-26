import hashlib


def compute_md5(information):
    m = hashlib.md5()
    m.update(information.encode('utf-8'))
    return m.hexdigest()
