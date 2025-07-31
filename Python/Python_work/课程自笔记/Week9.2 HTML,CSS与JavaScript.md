## Week9.2 HTML,CSS与JavaScript



### HTML（人的骨骼）

1. 工程师开发浏览器而制定了一个标准： tag
2. `VsCode`=>`xxx.html`=>`!`: 
3. 安装插件：`live server`或则`open in browser`
4. 格式非常丑陋，所以需要CSS



### CSS: Cascading Style Sheets（人的皮肤或衣服）

1. <style>放入<head>部分，进行修饰

2. 可做反爬，用CSS属性偏移



### JavaScript: 运行脚本 （人的肌肉）

1. 元素的动画效果
2. 内容的动态填充 (Ajax)
3. js能监听网页上的各种操作行为： 移动滑鼠，点击按钮，网页缩放，输入文字等。
4. 反爬：js指纹，鼠标轨迹



### 学习资料：

1. CSS 学习资料：Bootstrap 中文网站 =>进阶 sass=>less  https://www.bootcss.com/

2. 重新介绍JavaScript: https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/A_re-introduction_to_JavaScript

   

## Week 9.2: 浏览器渲染页面全过程

### 浏览器主要组件结构：

1. Safari 和Chrome使用webkit, 是一款开源**渲染引擎**

### 渲染路径

1. 解析HTML生成DOM树
2. 解析CSS生成CSSOM规则树
3. 将DOM树与CSSOM规则树合并在一起生成渲染树
4. 遍历渲染树开始布局，计算每个节点的位置大小信息
5. 将渲染树每个节点绘制到屏幕

### 构建DOM树

- DOM树生成过程中，会出现CSS和js的加载执行阻塞，即**渲染阻塞**的问题。
- 当浏览器遇到一个`script`标记时，DOM构建将暂停，直至脚本完成执行，然后继续构建DOM
- 所以：`script`标签位置很重要，实际使用，遵循两个原则：
  - CSS优先：引入顺序上，CSS资源优先于js资源。
  - js置后：JS代码放到页面底部，且js应尽量少影响DOM的构建
  - 解析html时，会把新元素插入DOM树中，同时去查找CSS, 然后把对应的样式规则应用到元素上，查找样式表按照从左到右的顺序去匹配。
  - DOM树的在爬虫领域很重要，因为js是通过DOM树来影响页面内容的。

### 构建CSSOM规则树

- 浏览器解析CSS文件并生成CSS规则树，
- 每个CSS文件都被分析成一个stylesheet对象，每个对象都包含CSS规则
- CSS规则对象包含对应于CSS语法的选择器和声明对象以及其他对象

### 构建渲染树

- 通过DOM树和CSSOM规则树，就可构建渲染树
- 浏览器会先从DOM树的根节点开始遍历每个可见节点
- 每个可见节点，找到其适配的CSS样式规则并应用
- 渲染树与DOM树最大的区别：
  - 不可见的元素不会出现在渲染树中： `display=none`, 是不会显示在这棵树中

### 渲染树布局

- 布局阶段从渲染树的根节点开始遍历，然后确定每个节点对象在页面上确切大小与位置
- 布局阶段的输出是一个盒子模型，会精确地捕获每个元素在屏幕内的确切位置与大小

### 渲染树绘制

- 遍历渲染树，调用渲染器的`paint()`的方法在屏幕上显示其内容
- 渲染树的绘制工作是由浏览器的UI后端组建完成的。

### reflow(回流)和repaint(重绘)

- HTML默认是流式布局，但CSS和js打破了这种布局，改变了DOM的外观样式及大小和位置
- `reflow`: 元件的几何尺寸变了，需要重新验证并计算渲染树，是渲染树的一部分或全部发生了变化
- `repaint`: 屏幕的一部分重画，不影响整体布局

### 扩展阅读:

Chrome浏览器渲染原理： https://segmentfault.com/a/1190000038468748

