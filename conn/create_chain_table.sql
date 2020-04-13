/*create_time是unix timestamp类型的数据。在创建的时候，采集到的实际时间仅仅精确到(3)。最后一位是从0到9的数字，根据数据抵达到某个特定终端的顺序来排序。*/
create table blocks
(
    id           int auto_increment primary key ,
    device_id    varchar(20),
    create_time  timestamp(4),
    data_content varchar(0),
    hash         binary(20) GENERATED ALWAYS as (unhex(sha1(concat(device_id, create_time, data_content)))) virtual ,
    prev_hash    binary(20)
);

DELIMITER $$
/*prev_hash并不是自动生成的。它的值应该是插入的。在insert之后，还应该执行这条语句来更新previous_hash值。*/
create procedure wrapped_insert()
begin
    set @current_id = (select id from test.blocks where prev_hash is null order by id limit 1);
    set @prev = (select prev_hash from test.blocks where id = @current_id-1);
    update blocks set prev_hash = @prev := unhex(sha1(concat(hash, @prev))) where id >= @current_id;
end;

DELIMITER ;