### Mac OS环境配置

#### 1. VPN

- WHUT VPN: `https://vpnu.whut.edu.cn/portal/#!/login` 下载相应版本

- `shadowsocks`:  `https://portal.shadowsocks.nz/knowledgebase/190/`

  `id: 1502208063@qq.com`

#### 2. Office(WHUT),PS(taobao),adobe acrobat(taobao)

#### 3. 百度网盘，腾讯会议，微信，QQ, discord



#### 程序运行配置

1. ##### 命令行界面

   `⌘+空格 `+ `terminal`

   

   ##### 是否安装Rosetta2 （for Mac OS Intel)
   
   ```
   /usr/sbin/softwareupdate --install-rosetta --agree-to-license
   ```
   
   
   
   ##### 2. 安装软件包管理工具: Homebrew(https://brew.sh/)
   
   ```
   xcode-select --install ↩︎
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
   OR↩︎
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   OR
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   
   ```
   这个命令将下载并执行 Homebrew 的安装脚本，自动安装 Homebrew 到 /usr/local/ 目录下；注意提示 Password: 的时候输入你的登录密码并回车。
   ```
   
   ```
   brew update ↩︎ # 自更新
   brew doctor ↩︎ #自检命令
   ```
   
   **For Mac OS M1**
   
   ```
   https://stackoverflow.com/questions/66666134/how-to-install-homebrew-on-m1-mac
   ```
   
   ```
   https://zhuanlan.zhihu.com/p/349636719
   ```
   
   

##### 3. 安装Python

```
brew install git python ↩︎ # python3.7.6左右版本
brew list
```

```
rm /usr/local/bin/python
ln -s /usr/local/bin/python3 /usr/local/bin/python
#执行命令来强制让 python 指向我们安装的 Python 3 的环境
```

**For Mac OS M1**

```
which -a python3
返回：
/opt/homebrew/bin/python3
python3 -V
/opt/homebrew/opt/python@3.7/libexec/bin  #add python3.7to python path
```



##### 4. 安装VSCode

- 官网下载对应版本并解压

- 按`⌘+空格`+输入`code`

- 在VSCode  按`⌘⇧+P `打开命令窗口，输入`install`

  ```
  从弹出的命令中选择 Shell Command: Install 'code' command in PATH
  ```

- 以后在命令行界面，输入`code`就可打开VSCode

- 回到Terminal窗口

  ```
  mkdir Code↩︎
  Code↩︎
  code .↩︎
  ```

- 在VSCode中按`⌘+N`，打开一个新文件；

  输入`print('Hello world!')`, 按`⌘+S`,文件名为 `hello.py`

- 关闭其中一个项目： `command+w`

- 回到Terminal 窗口

  ```
  输入 ls ↩︎
  输入 python3 hello.py
  ```

**Mac OS M1**

```
https://code.visualstudio.com/download
```



##### 5. 安装Pycharm: 2020.3.2 -macOS Apple Silicon dmg Version

```
https://www.jetbrains.com/pycharm/download/other.html
```

参考

```
https://blog.jetbrains.com/pycharm/2020/12/pycharm-2020-3-2-supports-apple-silicon/
```



##### 6. 安装venv 虚拟环境

```
mkdir venv #建立venv的文件夹
python -m venv venv # 在当前目录下安装venv
source venv/bin/activate #当前目录下激活venv = . venv/bin/activate
pip3 list #当前目录下查看安装程序
pip install -V setuptools pip #更新安装包
```



7. **cmd 基本操作**
   - 建立新文件夹： `mkdir` foldername
   - 删除文件夹：`rm -rf` directoryname
   - 只回到上一层目录：`cd ..`
8. **React on VSCode基本操作**
   - 在前端展示页面.jsx新建react: `rafce`

