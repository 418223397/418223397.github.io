## 办公自动化 Python

#### 注意事项：

#### 1. 任务的分解 ：读，算，存，转

#### 	读：

```
- 读取文件
- 读取文件中的数据/数值
```

#### 	算：

```
- 写入
- 改写/修改
- 排序
- 过滤
- 拆分
- 整合
- 统计运算
- 可视化
```

#### 2. 搜索引擎_关键字

```
- python read write excel
- python xlwt vs. openpyxl
- pandas read excel by row column index 
- search row by column value
```

#### 3.文件格式分类

#### 4. 区分数据框中的常量和变量

****

## Excel: `numpy` `pandas` `xlwt` `xlrd` `openpyxl`

#### 					` pandas` : 用于前端数据展现，擅长读、写；数据挖掘、数据清洗、数据分析

####                                       需要第三方模块来解析数据库（`numpy`  `xlwt` `xlrd`)

​												

#### 读

```
#从文件中读出表格信息 
read_excel(flilepath, header=None OR 2,uselocs = 'A:F')

#读取某行，某列，某个具体单元格,具体几行几列
df.iloc[[n,m]]
df.iloc[:n]
df.iloc[n,m]
df.iloc[[n1,n2],[m1,m2]]
```

#### 关于时间格式

```
to_pydatetime()
```

练习目标：

1. 补齐第一列、第二列名称
2. 读取 ”外商直接投资“，”产业结构“，”制造业规模“和 “人力资本” 四列数据
3. 将数据集拆分成四个单独列表，以城市为单位，以时间为纵轴，进行统计描述，并数据可视化
4. 将四个单独列表，合成一个面板数据（panel1)，先去对数，再进行回归分析，最后可视化
5. 将四个“媒体关注”数据，按照相等权重汇总到一张表格
6. 将汇总“媒体关注”数据导入到panel1，生成panel2
7. 对panel2进行统计描述分析、回归分析、可视化展示







#### 格式

| No.  | format |                Characters                |
| :--: | :----: | :--------------------------------------: |
|  1   |  .xls  |     2003 version, binary 二进制格式      |
|  2   | .xlsx  | 2007以后版本， XML数据结构；空间小，数列 |



