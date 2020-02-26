from record_block.block import RecordBlock
from database import getDataBase
from read_config import get_config


class BlockChain:
    def __init__(self):
        self.blocks = []
        # config = get_config()
        # dataBase, userTable, recordTable = getDataBase(config["mysql"])  # 这里我觉得record似乎更合适
        # dataBase.connect()
        # record_query = recordTable.select()
        # last_record = recordTable[-1]
        last_record = RecordBlock('1','1','1','1')
        '''
        last_record 指的是record表中最新的一条数据，你应该把上一句话删除并从表中取出
        该记录，将其转化为Block类并赋于last_record
        '''
        self.blocks.append(last_record)
        '''
        由于数据库中的数据过多，所以每次BlockChains类创建时，仅保存最新一条数据供操作，
        若要检验整个表中数据是否存在问题，如在服务端刚刚建立的时候，请调用self.chain_test
        '''

    def get_all_blocks(self):
        block1 = RecordBlock('1','1','1','1')
        block2 = RecordBlock('1','1','1','b59c67bf196a4758191e42f76670ceba')
        # block1,block2 仅供测试使用，请删除
        blocks = [block1,block2]
        '''
        该函数的目的是获取Record表中全部数据，并将其转化为recordBlock类放入列表中，
        请补全数据库操作
        '''
        return blocks

    def chain_test(self):
        blocks = self.get_all_blocks()
        flag = 1  # 判断标志
        for block in blocks[1:]:  # 1.判断自身的hash值是否正确2.前一个hash是否与previous——hash相同
            print(block.hash_test())
            print(block.previous_hash)
            print(blocks[blocks.index(block)-1].hash ==block.previous_hash)
            print()
            if block.hash_test() !=1 or block.previous_hash != blocks[blocks.index(block)-1].hash:
                flag =0
                break
        return flag

    def block_add(self,device_id,create_time,data_content):  # 添加一个新区块
        previous_hash = self.blocks[-1].hash
        new_block = RecordBlock(device_id,create_time,data_content,previous_hash)
        '''
        现在应该将new_block插入数据库中，成为最新一条，请补全
        '''
        self.blocks.clear()
        self.blocks.append(new_block)


