### Git 环境配置、在Github中操作和分支及协同

1. #### 配置好git账户信息与VSCode 相关联

   ```
   直接在powershell命令行下输入：
   git --version
   git config --global user.name "qxnatalie" #github 用户名
   git config --global user.email 1502208063@qq.com # github 登录邮箱
   git config --global core.editor "code -w" # 关联VSCode

   git config --list
   lt
   mkdir learn-git
   cd learn-git #创建一个目录
   pwd # 确认当前目录
   #进入learn-git文件下输入
   git status #非常重要的命令，随时确认当下状态
   ```
   
2. #### 初始化，创建MD文档

   ```
   git init
   Is -Force
   code readme.md #用VSCode 打开需要编辑的readme markdown文档
   
   ```

3. #### 提交、保留多文件、查看历史修改记录

   ```
   code readme.md # 用VSCode创建readme.md
   git status
   git add .\readme.md #把所readme.md文件进行staging缓存
   git commit #提交，再打开VSCODE后，第一行输入提交文字：eg."init commit"
   
   多文件操作
   #先创建多文件
   git add .
   git restore README.MD
   git commit #将除了readme.md文件外的所有文件进行提交，打开vscode后，在第一行输入“Add 2 python samples”
   git add README.MD
   git commit #"add note to readme"
   git status
   
   查看并修改历史记录
   git log # 退回点q
   git checkout XXXXXXX(前七位）
   git checkout master #命令回到当前
   git diff XXXXXXX
   git diff XXXXXXX SSSSSSS #比较两个版本的不同
   #VSCode 提供了“Gitlens"插件来操作有差异的文件
   ```

   #### 4. Git 和Github

   ```
   在github: Add repository ==> 两行命令
   ```

   ```
   #只是阅读推荐用clone:
   git clone "<link: clone https>"
   #如果对内容有修改后，再提交
   git status
   git commit -a -m “XXXX" # -a: 工作目录下所有修改放进staging. -m : "描述信息" == add + 打开vscode
   
   #修改后提交到主仓库进行push 是需要权限
   git push
   
   #如果主仓库有变化，就拉回来
   git pull
   git status
   ```

   ```
   #如果需要对主仓库进行修改，建议点"fork"/分支：复制一份在我的账户下
   再在我的账户进行clone，进行push ，pull操作
   #如果将修改版本推到主仓库:new pull request (in github A/C)
   
   
   ```

#### 5.分支/branch和协同

分支：是保证多人协同的必备工具  branch

标签：指向固定版本 tag

```
git tag v1.0 #打标签，用标签替代一串字符
git log
# 给上一个打标签
git tag v0.9 xxxxxxx
```

```
#因不同任务，开不同分支branch
git branch bug/fix1 #指向指针
git checkout bug/fix1 #checkout 指针HEAD从原来指向master转而指向bug/fix1.checkout 来切换当前工作分支 head 
git checkout master #指针指向master
git merge bug/fix1
```

