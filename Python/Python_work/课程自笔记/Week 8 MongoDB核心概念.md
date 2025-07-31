### Week 8 MongoDB核心概念

#### 大纲

- 安装MongoDB
- 什么是MongoDB
- 什么是NoSQL
- MongoDB的基本数据结构
- 连接MongoDB服务器



### 安装MongoDB

通过Docker安装环境

1. 使用 —v参数持久化数据
2. 暴露端口

下载MongoDB镜像

```
docker pull mongo
```

![image-20210523071037222](C:\Users\qxwri\AppData\Roaming\Typora\typora-user-images\image-20210523071037222.png)

-p: 指定端口号

-v: 指定数据持久化路径

Web程序=>mongo 存 log

爬虫程序=> mongo 存爬取的数据html, 正文内容 （对内）=>简单的数据清洗 =>MySQL

MySQL:数据库，用于存放数据

SQL:领域型语言，e.g.数据查询语言。用于操作数据库，可以支持其他数据库：阿里元ADB

### 什么MongoDB数据库

MongoDB 是面向文档的NoSQL数据库，用于大量数据存储。MongoDB是一个在2000年代中期问世的数据库。属于**非关系性/非结构性**数据库的类别。

- 关系型数据库：MySQL, SQL Server, Oracle, Access, 数据间存在关系，按照表的格式来存放；
- 非关系型数据库：MongoDB, Redis(内存键对值型)
  - 比如：视频，音频，博客，内容
  - MongoDB文档类似于json(bson)

### 什么是NoSQL: 非关系型的数据库，是Not Only SQL，是对不同于传统的关系型数据库的数据库管理系统的统称

NoSQL用于超大规模数据的存储：这类数据类存储不需要固定的模式，无需多余操作就可以横向扩展

比如facebook每天的产生非关系型数据



### MongoDB的基本数据结构

| SQL术语/概念 | MongoDB术语/概念 | 解释/说明                            |
| ------------ | ---------------- | ------------------------------------ |
| database     | database         | 数据库                               |
| table        | collection       | 数据库表/集合                        |
| row          | document         | 数据记录行/文档                      |
| column       | field            | 数据字段/域                          |
| index        | index            | 索引                                 |
| take joins   |                  | 表连接，MongoDB不支持                |
| primary key  | primary key      | 主键，MongoDB自动将_jd字段设置为主键 |

### MongoDB基本操作：

1. 创建数据库
2. 创建表
3. 插入数据
4. 查询数据

### MongoDB进阶操作

1. 范围操作符：需要熟悉并加记忆
2. AND操作符: 默认形式
3. OR操作符： `$or:[]`
4. 排序数据
5. 聚合数据
6. 更新数据
7. 删除数据

