#### Week 5 : 线程和进程

- 线程与进程的概念
- 同步与异步
- 并发与并行



#### 线程与进程基本概念

- 理解进程：读取程序（0/1的静态文件） + 数据集 = 进程 (运行时)

- 进程定义：通过静态的代码文件就会运行数据集从而产生进程

- 进程和线程的特点：

  - 运行一个程序，操作系统至少会启动一个进程

  - 不同进程之间不共享内存
  - 一个进程至少包括一个或多个线程
  - 线程没有独立内存空间，有自己的堆栈和局部变量
  - 多线程中会出现竞争状态 -- 解决方案（使用前要获得一个“许可”）
    - 互斥锁：一个线程需要获得一个锁，才可以使用内存空间。
    - 信号量：比如信号量为4时，内存空间最多同时存在4个线程，某个线程操作完成后，信号量会自增1，从而允许其他线程进入该内存空间。
    - 线程通过共享变量实现多线程直接的通信
    - 进程的通信主要通过信息传递（损耗更多资源）

#### 同步与异步（有序与无序）

- 开发同步网站的框架：`python 中的flask`

  ```
  pip install flask
  ```

- 异步：线程池

  ```
  from concurrent.futures import ThreadPoolExcutor
  ```

  

#### 并发与并行 (`Erlang之父Joe Armstrong`)

- 并发 concurrent:  is just like "2 queues 1 coffee machine": **比如：单核CPU** (高并发：单位时间内提高一个CPU的工作效率)
- 并行 parallel: is just like 2 queues 2 coffee machines：**比如：双核/4核/8核CPU**



#### Python 线程2： threading库

- 使用threading
- 线程锁： Lock
- 可重入锁：acquire, Rlock
- ThreadLocal: 实现每个线程都有自己独立的空间



#### Python 线程3:

- Python中存在的问题： GIL(Global Interpreter Lock: 全局解释器锁) 每次运行就是第一个线程
- 所以，在CPU运算密集型任务下，Python单线程运行效率会高于Python多线程运行效率



#### Python 线程4： ThreadPoolExecutor

- ThreadPoolExecutor(线程池)：异常捕获



### 作业：

1. Python 线程为什么无法利用多有的CPU资源？

   因为有GIL(Global Interpreter Lock) 全局解释器锁存在。从而使多个线程进行时，每次只能运行一个线程。

   

2. Python 线程适用于什么类型的项目？

   适用于系统的CPU性能相对硬盘和内存好很多的密集型任务执行。

   

3. 我们是否可以在单个子线程中再通过ThreadPoolExecutor创建线程池呢？

   是可以的。 保持一个程序创建的最大线程数量，给这些线程分配任务，不管有多少任务，线程最大数量保持不变就行了。

   

4. 我们是否可以在线程池中创建单个子线程呢？（能不能套娃）

   只要设置了运行线程的上限数量，应该是可以在线程池中创建单个子线程。

   #### 

   ### Python 进程1

   - multiprocessing 库

     - 多进程可以多核CPU同时执行任务，需要独立分配资源，其启动和销毁的代价较大。所以要根据服务器的配置来设置进程个数。

       ```
       join([tiemout])一个进程会被join阻塞几次。
       ```

   -  multiprocessing 支持三种启动进程方法：
     1. spawn (Windows) : ```if __name__='__main__'```
     2. fork (只存在Unix/Linux)
     3. forkserver

   - Process 子类化：通过继承的方式来实现进程

   

### Python 进程2

- 进程池： 如果要启动大量的子进程， 可用进程池的方式批量创建子进程

- Pool对象调用join()方法会等待所有子进程执行完毕。
- 进程锁（用得比较少）
- 进程通信（用得比较多）：进程运行相对独立，如果想相互使用彼此的功能，就需要通信： Queue, Pipes等多种方式来交换数据。
- pickle: python序列化



### Python进程3

- consurrent.future中池的原理:优化/简化线程和进程的使用。**池**的概念就是：复用

  - `concurrent.futures.ThreadPoolExecutor(max_workers)`
  - `concurrent.futures.ProcessPoolExecutor(max_workers)`

- 进程池的使用

- 线程池与进程池的差异

  #### 作业：

  1. 线程与进程的关系与区别？概念和方法
  2. 为何进程的使用要放在if`__main__`中？在Linux系统中用fork方式来创建外，其他系统就用这种方式
  3. 动手课程中进程的相关逻辑

  

  