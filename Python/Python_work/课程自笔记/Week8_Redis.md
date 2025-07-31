#### Redis

- 将数据存在内存中 （因为内存读取速度比硬盘快）
- 存储数据类型是非关系型数据和复杂的数据结构
- 数据是键值对型数据库
- 操作是原子性（往下切割：夸克 => 玄理论-弦（波利二象性））



### Redis 基本数据结构

#### String

- Redis的字符串是动态字符串，会根据实际情况动态调整。

  ```
  SET NAME NATALIE
  OK
  GET NAME
  NATALIE
  ```



### List

- Redis 中List 是一个链表，由于链表插入和删除比较快， 但查询效率较低，所以常常异步队列。

- 数据量比较小时，数据结构是**压缩链表**；数据量比较多时，数据结构是**快速链表**（Redis 进阶）

  ```
  LPUSH dbs redis
  1
  LPUSH dbs mongodb
  2
  LPUSH dbs mysql
  3
  LRANG dbs 0 -1
  mysql
  mongodb
  redis
  
  ```

  

### Set

- 是无序集合，意味着集合不能出现重复的数据

- Redis中集合通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1）。

- Hash: Key => Hash 算法 =>Value O(1)

- O(n) n越大，表示算法越差，描述的是算法的复杂度

  - 时间复杂度：
  - 空间复杂度：

- O(n)表示的是：算法随着数据增长其运行效率的变化的趋势。而不是记录一下它运行的时间。

  ```
  SADD dbs_set redis
  1
  SADD dbs_set mongodb
  1
  SADD dbs_set mysql
  1
  SMEMBERS dbs_set
  mysql
  redis
  mongodb
  ```

### Hash



### Zset

- Redis 有序集合和集合一样，也是String型元素集合，不允许重复

- 体现在：分值

- 内部是通过跳跃列表实现：以时间换空间

  ```
  ZADD dbs_zset 1 redis
  1
  ZADD dbs_zest 2 mongodb
  1
  ZADD dbs_zest 3 mysql
  1
  ZADD dbs_zest 4 mysql#添加不进去
  0
  ZARANG dbs_zest 0 -1
  redis
  mongodb
  mysql
  
  ```

### 过期时间 （过期机制/删除机制）

- Redis 有四种命令可以用于设置键的生存时间和过期时间：

  ```
  EXPIRE <KEY> <TTL>: 将键的生存时间设为 ttl 秒
  PEXPIRE <KEY> <TTL>: 将键的生存时间设为 ttl 毫秒
  EXPIREAT <KEY> <timestamp>: 将键的过期时间设为 timestamp 所指定的秒数时间戳
  PEXPIREAT <KEY> <timestamp>: 将键的过期时间设为 timestamp所指定的毫秒时间戳
  ```

- TTL: -1 # 时间无限

- redis中的任何key 都有删除机制，否则内存会被耗尽。



### Python如何操作Redis

- 安装redis-py
- 基本使用
- 使用pipeline
- 分布式锁

### 安装 redis-py

```
pip install redis
```

#### 

### 基本使用

连接Redis

```
```

