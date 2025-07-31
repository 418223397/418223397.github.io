#### Python 协程1

##### 用事件循环来实现： asyncio (python 代码： IO多路复用- python selectors)



1. 生成器与协程的关系
   
   - 都是定义中包含了`yield`关键字的函数
   
     - 生成器使用`yield`时，只用于返回生成的值，而不会接收值；
     - 协程使用`yield`时，除了可以返回值，还可以接收值，控制数据流动的方式。
     - 生成器和协程，在定义上很相近，也就是说在具体是实现上，是类似的。Python生成器和协程定义是混杂在一起的。
     - `.send(datum)`而不是`next`
   
     
   
2. 协程的状态：有四个状态 `inspect.getgeneratorstate(...)`

   

3. 产生多个值的协程: 见 vscode

   

4. 使用协程计算移动平均值

   

5. 使用装饰器激活协程: 简化`next()`激活的过程， 见vscode



### 作业：

- `make_avg()`方法中有个`while True` 的死循环，该协程要怎么停止？



6. 停止协程与异常处理

7. 协程返回值

8. 协程与异步的关系， 从yield, yield from , asyncio, async/await 角度去理解：

   - yield => 生成器

   - yield from => 委派生成器，将调用方的值，直接通过委派生成器到达子生成器。调用方与自生成器数据互通的关系

   - asyncio => 标准库， @asyncio.coroutine 装饰器的方式去定义协程

   - asyncio/await 对旧方法在语法上的改进

     

9. 协程为什么更快？

   - Golang 和 Python Web： 两者在语言表达性上差异不大；

     - Golang的性能会很好；(适合web开发)

     - Java语法限制比较多，工程能力好；适合大项目，阿里在背书

       - Go， PHP做web开发

     - Python动态语言，比较灵活，一个大的项目，Python的代码就显得很乱，PEP8

       - sklearn 3步走：几乎实现了所有熟悉的各类算法
       - Python 运维：堡垒机，Python控制的程序，用第三方库，实现Linux
         - 阿里云
         - low code 平台：大的游戏公司
         - zero code
       - Python 安全（kali msf去入门，小范围: 装摄像头，）

       - 如果上很大的项目，就用**装饰器**对参数做类型判断。可以通过一些手段，限制Python的灵活度。

         ```
         判断 X 类型是否为 int
         
         @d
         def t (x = int, y = dict):
             pass
         ```

         一般大项目：Python + MySQL + Redis + kafka ... 综合速度就比较快

         - e.g. 猴子补丁，Monkey Patch

   - 不用让CPU花费额外的资源切换线程或进程

   - 不需要考虑同步机制

     

     

#### 协程的主要使用场景：

- 爬虫：对性能比较高的小爬虫；而工程化的爬虫用scrapy；
- 高并发的场景下
- 协程在生产环境使用得比较少：抽象难理解，出问题难解决

