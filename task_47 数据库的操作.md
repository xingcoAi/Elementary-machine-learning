# task_47 mysql

==数据库的分类:==

- **关系型:**
    1.oracle
    2.DB2
    3.mysql->mariadb(分支)
    4.sqlserver
- **非关系型**
    1.键值存储:redis(做缓存)
    2.文档型:mongoDB
    3.列存储:HBase,Hive(大数据存储)
    4.图数据库:Neo4j

- **实时:实时计算**
-非实时:Hadoop,离线

###  数据库及表的操作

1. **运行mysql并登录**

```python
sudo service mysql start(状态:status/停止:stop);
mysql -uroot -p
```

2. **创建数据库**

```python
create database if not exists test default charset utf8 collate utf8_general_ci;
```

3. **查看数据库**

```python
show databases;
```

4. **删除数据库**

```python
drop database 数据库名;
```

5. **查看数据库字符编码**

```python
show create database 数据库名;
```

6. **修改数据库的字符编码**

```python
alter database 数据库名 character set utf8;
```

7. **进入数据库**

```python
use 数据库名;
```

8. **查看数据库下所有的表**

```python
show tables;
```

9. **新建表**

```python
create table 字段名(name 数据类型(数据长度))
```

10. **多字段创建表**

```python
create tabale a_table_name(
id int not null auto_increment,
name char(20) not null,
address varchar(50) not null,
primary key(id)
)engin=InnoDB DEFAULT CHARSET=utf8;
```

11. **查看创建表的命令**

```python
show create table 表名;
```

12. **删除表里的数据**

```python
delete from 表名;#可以回滚,一行行删除,有记录
truncate 表名;#不可以回滚,整表删除,无记录
```

13. **表的重命名**

```python
rename table tablename1 to tablename2;
```

14. **向表中插入数据**

```python
insert into tablename (id,name,is_delete/表中各字段名称) values (4,"n4",1/各字段的取值),(, ,),(, ,)#添加多个取值可同时插入多条数据
```

15. **更新数据**

```python
update tablename set is_delete=1,name="name1"[用逗号分隔添加所有字段] where id=7[主键]
```

16. **更改表结构:增加/删除一列(字段)**

```python
alter table tablename add sex varchar(10);
alter table tablename drop column sex(列名);
```

### 查询语句

1. **查询**

```python
select * from tablename;# * 代表所有字段
select id,name,sex from student;
select * from student limit 1,3;#从第一条数据开始,显示三条数据
select * from student limit 2,3;#从第二条数据开始,显示三条数据
select * from student limit 2;  #显示两条数据
select * from student where department="中文系";#查询条件为所有中文系学生
select * from studeng where department in ("中文系","计算机系")#在几个系间查询
select id,name,2019-birth as age,department,address from student where 2019-birth between 30 and 31;#用as取别名age,并按条件查询
select id,name,2019-birth as age,department,address from student where 2019-birth between 2019-birth>25 and 2019-birth<30;
select department,count(id) as person_count from student group by department;#group by以某字段来分组
select c_name,max(grade) as m from score group by c_name having m>95;#分组条件限制用having
select c_name,garde from score where student_id = (select id from student where name = "李四")#括号里面查询的结果作为其他查询语句的条件,两个表之间的关联查询
select student.*,score.* from student,score where student.id = score.student_id and student.name = "李四";#同时查询两个表
select c_name,avg(grade) from score group by c_name;#计算平均值
select student_id,grade from score order by grade;#从低到高排序
select student_id,grade from score order by grade desc;#从高到低排序
```

### mysql的关联查询

```python
select id from student union select student_id from score;
select id from student union all select student_id from score;#不去重
select student.id,name,sex,birth,department,address,c_name,grade from student,score where (name like "张%" or name like "王%") and student.id = score.student_id;#用like实现模糊查询,%代表任意
select * from student a left join score as b on a.id = b.student_id;#左关联,join on成对出现,as关键字可省略,左表不能出现空,右表可出现空
select *from student a right join score b on a.id = b.student_id;#右关联
select *from student a inner join score b on a.id = b.student_id;内关联或全关联,两个表的数据都不能出现空
select *from student a join score b on a.id = b.student_id;#内关联的另一种写法
```

### 索引

> 对数据库某个字段或多个字段的值进行排序，加快数据库的访问速度
>
> 字段值重复性低的字段适合建立索引

```python
create index 索引名 on 表名(id/字段名)＃创建索引
alter table 表名　add index 索引名　(字段名)＃通过修改表创建索引
＃在创建表时创建索引
create table_name(
-> id int not null auto_increment
-> name char(255) not null
-> index index_name (name/字段名)
-> );
＃添加关键字unique为唯一索引
#创建联合（组合）索引
alter table 表名　add index index_name (name,city,address,/要创建索引的多个字段名)；
create index 索引名 on 表名(id,多个字段名)；
```

### binlog

> mysql语句执行记录日志，实现主从同步