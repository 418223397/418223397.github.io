#### Vercel + NextJS + TailwindCSS for blogger

1.  Homebrew Upgrade

   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   ```
   brew help
   ```

2. 安装 NextJS

   ```
   1. #安装nvm: nodejx 官网安装部分
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
   
   2. # 安装 nodejs, 版本号查看https://nextjs.org/docs/getting-started/installation要求
   nvm install v23
   
   3. #查看版本号
   node -v
   nvm -v
   
   4. #安装yarn
   npm install -g yarn
   
   5. #创建新的nextjs项目
   yarn creat next-app my-fiction-app
   cd my-fiction-app
   
   6. #安装依赖项目
   yarn instll
   
   7.  #打开VSCODE
   code .
   
   8. #初始化==>运行==>搭建： 在vscode的终端窗口
   yarn
   yarn dev
   yarn build
   ```

   3. 在APP中“page.js", 输入”rafce"
   
      若没有，安装 
   
      ```
      ES7 React/Redux/GraphQL/snippets (extension)
      
      ```

4. Tailwindcss: 获取账号密码，找到components ==> marketing ==> landing pages==> React ==>copied Codes ==> paste "page.js"of app in VSCode

```
```

