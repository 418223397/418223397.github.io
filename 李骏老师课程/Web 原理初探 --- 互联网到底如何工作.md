### Web 原理初探 --- 互联网到底如何工作

#### 1. 基本概念

- network 网络：若干台计算机设备（一切可以联网的设备，通过一定机制），可以相互连接在一起，访问对方。

- internet 国际网络：很多个以上的网络互联起来 （inter-net)

- Internet 互联网 (the Internet)：世界上最大的网际网络，一个基础设施

- world-wide web 万维网 （web/the web): 是互联网上的应用。是一个应用系统。和email在互联网上应用一样。

  <img src="C:\Users\qxwri\AppData\Roaming\Typora\typora-user-images\image-20230308083629904.png" alt="image-20230308083629904" style="zoom: 33%;" />

#### 2. 在浏览器的地址输入一个地址，然后回车会发生什么直到网页内容显示

##### 2.1 “第一层”答案/初级答案：

- 寻址（寻找资源，在互联网的什么位置）==> URL, Domain,IP, DNS

- 建立连接 （我的计算机和提供资源计算机连接起来）==> TCP/IP,Client-Server

- 对话 （遵循一个protocol: 规划范协议/按照特定协议）==> HTTP （请求和发起机制：request-response)

- 正确解析和展示 （资源是另外一种协议/protocol) ==> Media Types/Content types/MIME types : HTML -->DOM, etc., 

  <img src="C:\Users\qxwri\AppData\Roaming\Typora\typora-user-images\image-20230309031604885.png" alt="image-20230309031604885" style="zoom:67%;" />

###### HTTP = Hypertext Transfer Protocol 超文本传输协议

###### HTML = Hypertext Markup Language 超文本置标语言 ,包含以下上个内容：

1. 表格数据内容：html ==> 未来发展只提供**语义化**标签

2. 表格展现格式：css

3. 表达互动方式：js

   

   #### HTML DOM (Document Object Model)

   

   <img src="C:\Users\qxwri\AppData\Roaming\Typora\typora-user-images\image-20230309033948624.png" alt="image-20230309033948624" style="zoom:67%;" />

###### Hypertext:

- 支持超链接*hyperlink*的文本
- 支持各种格式的文本 （多样化格式）
- 能够嵌入各种媒体的文本 （各种媒体）

###### Markup: 使用各种标记 tags 给文本添加功能

```
This is a <strong>text</strong>.
This is a <em>text</em>. #emphasis
This is <a href="URL">hyperlink</a>.
<img src='lena.png'/>
<ol>
	<li>Windows</li>
	<li>MacOS</li>
	<li>Linuk</li>
</ol>
There are <span id='cat-count'>4</span> cats in our office.#有些tags与展示无关，用编程服务
```





##### 2.2 具体实现工具

- URL: Uniform Resource Locator (主机host：真正的门牌号码/服务器/多台计算机 :；窗口/l楼层/端口号/服务程序/线程 port/；资源所处的位置 resource path ?;参数：#；锚点：指向资源中某位置的标记)

  <img src="C:\Users\qxwri\AppData\Roaming\Typora\typora-user-images\image-20230308130656037.png" alt="image-20230308130656037" style="zoom: 67%;" /> 

- Domain Name: 域名是分段管理；根域名管理已授权每个区域分配管理；域名是字符串，底层通讯管理起来非常困难，本质上是对应一个IP地址。

- DNS Server: Domain Name System 互联网黄页

- IP 地址：IPv4 (4*8 = 32 位) --- 4G; IPv6 address (128位) ==>与网卡关联（有芯片）/物理地址MAC

- 客户机与远端服务器建立连接（通过broadcasting 广播/喊）：延时是稳定的，可以忽略



#### Web 数据抓取 Data Scraping： 为了创造业务价值（会写程序，统计学，业务领域深耕）

#### <u>Data Scraping 本质是：在一个html文档中去找一些特征，帮助bs4去唯一定位所需数据（一层一层定位</u>）

#### <u>原则是：即便页面内容发生变化，则数据发生变化可能性最小；</u>

#### 1. Obtaining 获取数据: 自己的数据，线上已有的开放规整数据，通过API访问json数据，网页上抓取数据

#### 2. Scrubbing 清洗数据：

vs. crawling: 从一个页面出发的超链接到相关联页面并下载。如：搜索引擎 （crawler/spider) 

关注：遍历资源效率

scraping: 从非结构的html页面下抓取所需的数据。（scraper: 页面中抽取数据）

关注：识别要抓取数据特征

---

#### 3.Exploring 概览：

#### 4. Modelling 建模：通过一个模型找到数据中的规律

#### 5. Interpreting 解释：用得出模型做出预测（在分析历史之上/解释数据）

