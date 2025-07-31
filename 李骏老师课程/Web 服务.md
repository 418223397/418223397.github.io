### Web Services 服务

1. #### 多层服务：终端设备+在线服务（前后端分离）

2. #### 输入方式：URL, Web Form; 输出方式：HTML Page（Java script), JSON Data(字符串)

3. #### 从*个人爱好* 到 *软件工程*（多人协作/协调，测试）

   - 开发环境管理 *Environment*
   - 软件测试 *Testing*
   - 交付和部署 *deployment*

4. #### 开发环境

   - 创建 venv
   - 安装： python -m venv venv #安装虚拟环境
   - 激活： .\venv\Scripts\Activate.ps1
   - 退出激活：deactivate

5. #### Web 服务部署

   - 并发问题
   - Web 服务部署采用这个架构：Web Server（Nginx, Lighttpd, <==> 反向代理 去请求WSGI Server <==> server.py )

6. #### CSS 和 Form (样式表)

