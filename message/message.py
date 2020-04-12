# 通往小区服务器的数据广播和接收。
from blockchain.record import Record
from typing import List
import lz4.frame


class PeerMessage:
    record_list = None  # type: List[Record]

    def _to_raw_string(self):
        raw_string = ""
        for record in self.record_list:
            raw_string += record.serialize()
        return raw_string

    def broadcast(self, peer_list):
        data_to_sent = lz4.frame.compress(self._to_raw_string())

