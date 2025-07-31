## Docker 基本概念+基本操作

Docker: 镜像管理的容器技术。

镜像：是一种确保两个对等体始终包含相同数据的过程。

#### 安装Docker：见“Windows上安装Docker"文件

- Docker 在效果上，与虚拟机的作用类似。
- Docker 轻量级，将各种软件，放在一个独立的环境中
- Docker 可以避免我们处理各种环境问题

#### 镜像 images：是Docker容器启动的先决条件 （如程序）

1. 定义：只读的文件和文件夹。启动容器的基础，包含容器运行时所需要的所有基础文件和配置信息
2. 如何获得镜像
   - 自己创建：在基于centos/ubuntu(Linux系统) =》安装nginx服务，部署你的应用程序，配置
   - 拉取别人制作好的镜像：pull

#### 容器：（如进程）带有运行时需要的可写文件层，并且容器中的进程属于运行状态

1. 容器运行真正的应用进程：有初建，运行，停止，暂停和删除的五种状态。
2. 在容器内部，是无法看到主机上进程，环境变量，网络等信息。这是容器与直接运行在主机上进程的本质区别。

#### 仓库（可以理解为：如Github)

1. 用来存储和分发Docker镜像
2. 镜像仓库分为公共镜像和私有镜像

#### 容器的标准化（扩展知识）

1. 容器技术很火，需要制定一个标准。
2. 容器编排技术在竞争：Docker Swarm, Kubernetes(K8s) by google, Mesos.
3. OCI: open container initiative: 牵头制定了一个开放的容器标准
   - 容器运行标准：runtime spec
   - 容器镜像标准： images spec

#### 镜像操作 

1. 拉取镜像：

   ```
   PowerShell
   
   docker pull busybox
   (busybox 是Linux系统的“瑞士军刀”)
   ```

   

2. 重命名镜像：`docker tag`

3. 查看镜像：`docker image ls busybox/docker images`

4. 删除镜像：`docker rmi` busybox

5. 构建镜像：`docker build -t mybusybox .(当前目录下)`(基于DockerFile镜像)

#### 镜像实现原理：

- Docker 镜像是由一系列镜像层(layer)组成的，每一层代表了镜像构建过程中的一次提交。

- 三个镜像层，最后组合在一起。（可参考`mybusybox`镜像搭建）

- 每一层根据镜像的内容都有一个唯一的ID值，当不同的镜像间有相同的镜像层时，便可实现不同镜像之间共享镜像层的效果。从而节省空间。

  见文件：C:\users\qxwri\Code\learn_docker\Dockerfile

### 容器操作

1. 容器是什么：容器是基于镜像创建的可运行实例，并且单独存在，一个镜像可以创建多个容器

2. 容器层: 允许修改镜像的整个副本 （可读写）

3. 容器的五个生命周期：

   - created: 初建状态
   - running: 运行状态
   - stopped: 停止状态
   - paused: 暂停状态
   - deleted: 删除状态

4. 创建并启动容器

   ```
   docker create -it --name=busybox#容器的名字 mybusybox #基于镜像创建容器
   ```

   ```
   docker start busybox
   docker ps
   ```

   ```
   docker run -it --name=busybox2 mybusybox #进入交互模式
   ps aux
   exit # 对于容器来说，杀死容器中的主进程，则容器就会被杀死
   ```

5. 终止容器

   ```
   docker stop busybox2
   docker start busybox2 #再次启动
   ```

6. 进入容器

   ```
   docker exec -it busybox2 sh
   ps aux #查看进程，会有两个sh进程。用exec的方式进入容器，会单独启动一个sh进程，每个窗口都是独立且互不干扰。
   ```

7. 删除容器： 先删除容器，才能删除镜像

   ```
   docker rm busybox2
   ```

   ```
   docker rm -f busybox2 #-f: force强制删除
   ```

#### 容器是什么：镜像层的副本创建了容器层

### 

长时间为使用，重新启动：

- 管理员身份in powershell

```
& 'C:\Program Files\Docker\Docker\DockerCli.exe' -SwitchDaemon
```

