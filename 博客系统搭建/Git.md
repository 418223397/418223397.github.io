### Git 

1. #### 关联git账户与VSCode 相

   ```
   直接在powershell/terminal命令行下输入：
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
   code readme.md #用VSCode 打开需要编辑的readme markdown文档
   
   ```

3. #### OR 已在本地创建repo, 关联repo以便同步Github

   ```
   cd blogger-starter-app
   git init
   git status
   
   git add . #将“blogger-starter-app"文件中全部加入到repo中
   git status #检查状态
   git commit -m "initial commit"#第一次版本信息说明 （-m means" message"）
   ```

   

4. #### Github账户中创建新的”repo“， 并复制链接，在本地查看远程版本

   ```
   pwd #确认当前路径
   git remote add origin https://github.com/fatbookpro/blogger-starter-app.git
   git remote -v #以下会出现“fetch" 和”push"
   ```

   

5. #### 将本地Repo推至Github Master' 仓库--- 本地repo 1.0最初版

   ```
   git push --set-upstream origin master
   jt.ascll@gmail.com
   16进制token #在账户setting中设置：==>token ==> “select scopes: 选择”workflow", "write:package, delete: package"
   
   -----
   经过以上操作，本地repo就可以出现在Github相关repo中。
   ```

   

6. #### 将master 分支修改成 main --可参考chatgpt

   ```
   git push --set-upstream origin main
   git pull origin main --rebase
   #conflicts 发生
   git status #找到冲突文件
   code README.md #如果冲突文件是README.md, 用vscode打开，合并，修改，完成编辑
   git add README.md
   git rebase --continue #完成冲突合并
   
   git push --set-upstream origin main
   git branch #q退出
   git branch -d master #删除本地仓库master 分支
   git push origin --delete master # 删除远程master 分支
   
   ```

   

7. #### 更新博客内容，同时Git同步

   ```
   code .# 博客内容更新完毕后
   git remote -v #确认远程版本
   git commit -m "update climatlantic" #标注版本信息
   git push origin main
   
   git status
   git log #打印更新日志
   
   ```

   

8. #### 提交、保留多文件、查看历史修改记录

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

---

#### 本地同时管理两个Github 账号

```
ssh-keygen -t ed25519 -C "tj.ascll@gmai.com"
/Users/qiuxin/.ssh/id_ed25519_first

ssh-keygen -t ed25519 -C "1502208063@qq.com"
/Users/qiuxin/.ssh/id_ed25519_second

ssh-add ~/.ssh/id_ed25519_first
ssh-add ~/.ssh/id_ed25519_second
 
#for Mac ISO
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_first
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_second

ssh-add -l

nano ~/.ssh/config

#配置第一个GitHub账户
Host github-first
    HostName github.com (四个空格)
    User git
    IdentifyFile ~/.ssh/id_ed25519_first
#配置第二个Github账户
Host github-second
    HostName github.com
    User git
    IdentifyFile ~/.ssh/id_ed25519_second
 
Ctrl+ o 保存， Ctrl + X 退出

显示密钥，打开Github SSH进行配置
cat ~/.ssh/id_ed25516_first.pub 
cat ~/.ssh/id_ed25516_second.pub

ssh -T github-first
ssh -T github-second

cd pwd
git remote set-url origin git@github-second:fatbookpro/blogger-starter-app.git# 关联远程和本地相同文件
git clone git@github-second:qxnatalie/directory-site.git#将远程仓库拉回本地，从新新建

git remote -v #进行文件管理权限账户的确认
```

