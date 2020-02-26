from record_block.block import RecordBlock

my_block = RecordBlock(device_id='1',create_time='1',data_content='1',previous_hash='1')

print(my_block.hash)
print(my_block.hash_test())