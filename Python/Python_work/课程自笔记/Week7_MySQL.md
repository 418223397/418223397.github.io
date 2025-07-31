

#### MySQL

1. 安装MySQL
2. 安装Navicat (连接数据库的工具)
3. MySQL的核心概念
4. MySQL数据类型
5. 基本操作



#### 安装MySQL (Docker)

```
docker pull mysql #拉取mysql的镜像
```

```
docker images
docker run -p 3307:3306 （本机地址：容器端口）--name mysql-test2 mysql -e .....(如下)
```

```
docker run mysql
```

```
docker run -it --name==mysql1 -e MYSQL_ROOT_PASSOWORD=123456 mysql
docker ps （ctrl+c)
```



#### 安装Navicat (需要破解)

- localhost => 127.0.0.1
- HOST => 映射到localhost
- 计算机 => 网卡 =>发送和接收数据包
- 网卡有指向自己的IP: 127.0.0.1

```
docker run -p 3307:3306 --name mysql-test1 -e MYSQL_ROOT_PASSWORD=123456 mysql
```

- Docker 容器运行结束，被删除后，数据会丢失。通过以下命令复制一个容器
  - MySQL存数据的本质，就是**写文件**， 具体操作如下

```
cd
mkdir <pathname>
pwd
#配置数据，日志数据和数据本身保存到对应的文件夹里
```

```
docker run -p 3308:3306 --name mysql-test3 -v D:\mydockerdata\mysql\conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=123456 -d mysql
```

```
docker run -p 3310:3306 --name mysql-test5 -v D:\mydockerdata\mysql\data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql
```

```
docker run -p 3309:3306 --name mysql-test4 -v D:\mydockerdata\mysql\logs:/var/log/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql
```



#### MySQL的数据类型：时间，数值和字符串

| 类型      | 大小                 | 用途         |
| --------- | -------------------- | ------------ |
| INT       | 4 bytes              | 整数值       |
| FLOAT     | 4 bytes              | 单精度       |
| DATETIME  | 8 bytes              | 日期和时间值 |
| TIMESTAMP | 4 bytes              | 时间戳       |
| CHAR      | 0 - 255 bytes        | 定长字符串   |
| VARCHAR   | 0 - 65535 bytes      | 变长字符串   |
| TEXT      | 0 - 65535 bytes      | 长文本数据   |
| LONGTEXT  | 0 - 4294967295 bytes | 极大文本数据 |
| JSON      | 0-4G                 | JSON数据     |



### MySQL基本操作

- 数据库操作
- 数据表操作
- 数据的增删改查

#### 数据库操作：链接到MySQL

1. 创建数据库

   ```
   mysql> CREATE DATABASE `TestDB` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';



2. 删除数据库

   ```
   mysql> DROP DATABASE `TestDB`;
   ```

   

3. 创建新数据表

   ```
   CREATE TABLE IF NOT EXISTS `answer` (
     -- AUTO_INCREMENT => 自增，id=1, id = 2 
     `id` INT UNSIGNED AUTO_INCREMENT, 
     `title` VARCHAR(100) NOT NULL,
   	`author` VARCHAR(40) NOT NULL,
   	-- 设置主键
   	PRIMARY KEY (`id`)
   ) ENGINE = INNODB;
   ```

   公司中常用的建表语句：

   ```
   DROP TABLE answer;
   ```

4. 插入数据

   ```
   INSERT INTO answer_company ( `user_id`, `question_id`, `answer`, `answer_detail`, `review`, `create_time`, `update_time` )
   VALUES
   	( 1, 1, '你是谁', '我是神', '不错', UNIX_TIMESTAMP( NOW( ) ), UNIX_TIMESTAMP( NOW( ) ) );
   ```

5. 查询数据

   ```
   SELECT * FROM answer_company WHERE is_deleted = 0 AND
    user_id = 3 AND question_id = 3;
   ```

   ```
   SELECT `user_id`, `answer`, `review` FROM answer_company WHERE is_deleted = 0;
   ```

   如果常用的查询字段，就可以将此字段设置为索引。

   ```
   SELECT * FROM answer_company WHERE answer LIKE '%你是谁%';
   ```

   - 多表查询：JOIN, 子查询, UNION
   - 执行计划：进行优化方向。比如SQL进行很慢
   - ORM: 对象关系映射。 peewee, sqlalchemy
     - class A (XXX)
   - 逻辑性复杂性的逻辑查询（如何用MySQL解八皇后）

6. 排序

   ```
   SELECT * FROM answer_company WHERE answer LIKE '%你是谁%' ORDER BY id DESC;
   ```

   ```
   UPDATE answer_company SET question_id = 2 WHERE user_id = 1;
   ```

7. 软删除

   ```
   UPDATE answer_company SET question_id = 2 WHERE user_id = 1;
   ```

8. 事务处理：多条语句作为一个整体进行操作的功能；或则数据回滚(ROLLBACK)

   - MySQL数据库有多个引擎， InnoDB支持事务。
   
     

### 用Python实现MySQL

1. 连接MySQL

   ```
   pip install PyMySQL
   ```

   ```
   import pymysql
   
   connection = pymysql.connect(host='127.0.0.1', port=3307, user='root', password='123456', db='TestDB', charset='utf8')
   
   print(connection)
   ```

2. 执行SQL：游标 （用字典形式为好，插入更新：connection.commit() 来执行）

   ```
   import pymysql
   
   connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='TestDB', 
   charset='utf8')
   
   cursor = connection.cursor()
   
   data = {'user_id': 1, 'question_id': 2, 'answer': '一个答案','answer_detail': '一个答案','review': 'review'}
   
   sql = 'INSERT INTO `answer_company` (`user_id`, `question_id`,`answer`, `answer_detail`, `review`) VALUES (%(user_id)s,%(question_id)s, %(answer)s, %(answer_detail)s, %(review)s);'
   
   res = cursor.execute(sql, data)
   
   print('影响行数：', res)
   ```

3. 查询数据

   ```
   sql = 'INSERT INTO `answer_company` (`user_id`, `question_id`,`answer`, `answer_detail`, `review`) VALUES (%(user_id)s,%(question_id)s, %(answer)s, %(answer_detail)s, %(review)s);'
   
   sql = 'SELECT * FROM `answer_company` WHERE user_id=1;'
   ```

4. 事务处理

   ```
   connection.begin()
   connection.commit()
   connection.rollback()
   ```

### 常用的操作封装：生产环境下的一个项目

```
https://github.com/ayuLiao/mysqldb/blob/master/db.py
```

- 连接池（有很多连接），每隔一段时间，去检查一下，连接池中的连接是否还活跃。

  MySQL Cilent ( Navicat/PyMySQL) => （协议）Server

  如果Server主动断开Client连接，Client是不知道的。MySQL Conf 最长连接时长。

  PyMySQL, 解决方案1：  池， 开一个Thread => while True => ping Server；如果某些意外情况，关闭了，那么这次的SQL执行会失败，CS, 自动尝试重连。（db.py + pool.py)

  解决方案2： 重新连接

- 报错：2021-5-2

  ```
  pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on 'localhost' ([WinError 10061] 由于目标计算机积极拒绝，无法连
  接。)")
  ```

  解决方案

  ```
  TestDB的数据放在：mysql_test1中，Port是3307, 不是3306
  ```

  

  #### 小结
  
  1. 多表查询：join
  
  2. 子查询：嵌套查询
  
     ```
     SELECT ...
     WHERE ...
     IN(SELECT ... )
     (SELECT...):
     ```
  
  3. 连接多个查询结果: UNION
  
  4. 如何对SQL的性能分析： SQL 执行计划
  
  5. ORM: Object Relationship Mapping - 创建一个类: Peevee, Django
  
     - 避免sql注入
  
  6. 逻辑性复杂查询： 利用MySQL解决八皇后的问题（回数算法：递归， 见“懒编程”：公众号）