# ChainServer-backend

社区区块链管理程序的小区主机，和客户端数据交互、以及充当区块链小区节点的数据服务器
和后端服务器。

需要先执行create_chain_table,create_user_table以创建数据表。

因某些人的摸鱼行为，导致了数据库连接方式大改，现在message和record_block都处于不可用状态。并打算在后续情况中归入models（模型层）
