### TCP/IP与http协议

#### 1. TCP/IP协议： 一系列构成互联网基础的网络协议，是Internet的核心协议

- Transmission Contrl Protocol/Internet Protocol

#### 2. OSI七层模型

- ISO组织1984年提出了OSI的参考模型
  - ISO: 是一个国际化标准组织，International Organziation for Standardization
  - OSI: 参考模型--开发式系统互联，Open System Interconnection

#### 3. TCP/IP 四层模型

- 由上到下层层包装：应用层，传输层，网络层，链路层
- HTTP 报文传输流程

#### 4. HTTP协议

- 超文本传输协议：Hyper Text Transfer Protocol
- HTTP + SSL = HTTPS 避免中间人窥探到数据包中的信息
  - 想看别人的HTTPS =>`监听路由器` =>中间人攻击（`信息安全`）

- HTTP是一个基于TCP/IP通信协议来传递数据（HTML文件，图片文件等）
- HTTP协议工作于客户端-服务端架构上。

#### 5. HTTP特点

- 灵活：
- 无连接：短连接，长链接
  - 爬虫：Keep-alive
- 无状态：
  - Cookies(身份标识)

#### 6. URL

- HTTP使用统一资源标识符（URI, Uniform Resource Identifiers）来传输数据并建立连接。URL是一种特殊类型的URI,包含了用于查找某个资源的足够信息。
- URL: Uniform Resource Locator, 统一资源**定位**符

- 各部分组成：
  - 协议部分： `http:`
  - 域名部分：`www....` 或则IP地址
  - 端口部分：域名和端口之间使用`:`分隔符，一般是默认端口 （不是必须部分）
  - 虚拟目录部分：从第一个`/`到最后一个`/`（不是必须部分）
  - 文件名部分：从域名最后一个`/`开始到`?` 或者最后一个`/`到`#`或者最后一个`/`到结束
  - 锚部分：从`#`开始到最后 （不是必须部分）
  - 参数部分：从`?`到`#`为止之间。参数可以允许多个参数，参数与参数之间用`&`

#### 7. URL 和 URI

- URL是URI的子集



#### 扩展阅读：

1. HTTP协议入门：http://www.ruanyifeng.com/blog/2016/08/http.html
2. 如何理解HTTP的无连接，短连接，长连接：https://segmentfault.com/a/1190000015821798



#### 8. 网页请求全流程

- DNS解析：输入网页名/域名 => 通过DNS解析 =>IP地址=>访问网页
- IP地址是一个32位的二进制数
- DNS:网络服务器（6个步骤）
- TCP三次握手
- 数据传输
- 断连接TCP第四次挥手

#### 网页请求流程小结：

1. DNS解析：将域名解析为IP地址
2. TCP 连接： TCP三次握手
3. 发送HTTP请求
4. 服务器处理请求并返回HTTP报文（response)
5. 浏览器解析渲染的页面
6. 断开连接：TCP第四次握手