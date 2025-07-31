## Week9.3使用Python虚拟环境

### 静态网页与动态网页

- 开发工程师眼中：
  - 静态网页：写死的纯HTML网页
  - 动态网页：在不改变HTML代码的情况下，能根据不同用户或不同操作显示不同内容
- 爬虫工程师眼中：
  - 静态网页：网页主体内容的渲染由服务端完成， 返回的HTML 文件中包含了所需内容
  - 动态网页：网页主体内容需要通过浏览器中的JavaScript进行计算或渲染才能显示最终的内容
    - Ajax是一种动态请求方式， server Data => Brower

### 虚拟环境

- 概念：是一个独立的Python环境，在虚拟环境中通过pip安装第三方库，是不会影响到本地的Python环境

```
python -m venv venv #安装虚拟环境
```

- 在ps下激活

```
PS C:\Users\qxwri\Code\learn_venv> .\venv\Scripts\Activate.ps1
```

```
#退出虚拟环境
deactivate
```



### 扩展阅读

创建虚拟环境： https://docs.python.org/zh-cn/3/library/venv.html

