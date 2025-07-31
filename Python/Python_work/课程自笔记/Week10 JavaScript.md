### Week10 JavaScript

#### 一.JavaScript 快速入门

#### 二. JavaScript 对象的门道

#### 三. JavaScript 原型链

#### 四. JavaScript 函数进阶



- ### JavaScript 快速入门

  - 网景公司+Brendan Eich => JavaScript + Microsoft etc., =>ECMA 标准： ES6,ES7

  - 基本概念：

    - 核心 ECMAScript
    - 文档对象模型 DOM
    - 浏览器对象模型 BOM

    ECMAScript: 即ECMA-262定义的语言，并不局限于Web浏览器。

    ECMA-262将这门语言作为一个基准来定义，以便在它之上再构建更稳健的脚本语言。Web浏览器只是ECMAScript 实现可能存在的一种宿主环境（host environment).

    宿主环境提供ECMAScript 的基准实现和与环境自身交互必需的扩展

    扩展（比如DOM)使用ECMASript 核心类型和语法，提供特定于环境的额外功能。其他宿主环境还有服务器端JavaScript平台Node.js 和即将被淘汰的Adobe Flash.

  - 基本语法：

    - 赋值语句

      ```
      var name = "Natalie"；
      let name = "Jordan" //块作用域
      ```

      ```
      if (true){
      	x = 1;
      	y = 2;
      	z = 3;
       } 
      //{...}内的语句具有缩进，通常是4个空格，表示代码块，不是必须，但有助于理解代码层次。注意与python的区别，缩进4个空格是必须的。
      ```

      ```
      /*
      注释块
      */
      
      //这是一行注释
      alert('hello';)
      ```

- #### 基本数据类型和变量

  #### Number

  - js不区分整数和浮点数

####      模板字符串

```
var name = "Natalie";
var age = 45;
var message = '你好，${name}, 你今年${age}岁了，恭喜啦！';
alert(message);
```

####  布尔值： true/false

![image-20210530030755104](C:\Users\qxwri\AppData\Roaming\Typora\typora-user-images\image-20210530030755104.png)

```
"==" //js会做类型转化
“===”//is in Python
```

#### null 和 undefined

#### 数组

#### 对象：一组由键-值组成的无序集合（注意与字典的区别）

```
var person = {
	name = 'natalie',
	age = 43,
	tags = ['code','Python']
};
```

在ES6中map放入`字典`

#### 函数

#### 变量提升：js执行的特点



#### 扩展阅读：

1. 重新介绍js: https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/A_re-introduction_to_JavaScript



### JavaScript 对象的门道

#### 理解对象：

![image-20210530065429893](C:\Users\qxwri\AppData\Roaming\Typora\typora-user-images\image-20210530065429893.png)

- ECMA-262使用一些内部特性来描述属性的特征。JS的开发者是不能直接访问这些特征，为了将某个特性标识为内部特性，规范会用连个括号把特性的名称括起来： 比如[[Enumerable]].
  - 属性分两种：
    - 数据属性
      - [[Configurable]]
      - [[Enumerable]]
      - [[Writable]]
      - [[Value]]
    - 访问属性
      - [[Configurable]]
      - [[Enumerable]]
      - [[Get]]
      - [[Set]]

#### 创建对象：（解决同时创建多个对象）

##### 工厂模式

![image-20210530070441224](C:\Users\qxwri\AppData\Roaming\Typora\typora-user-images\image-20210530070441224.png)

##### 构造函数模式： 使用new就成了构造函数