#### CSS Cascading System Sheet: 层叠样式表

1. defintion: is the code thatt styles web content. It is not a programming language, like HTML. It is a style sheet language.

2. Role: to select style HTML elements. 

   ```css
   p {
       color: yellow;
   }
   ```

   - save the previous file as `style.css`

   - open `index.html`, between <head> and </head> tages: 

     ```
     <link href="styles/style.css" rel="stylesheet"/>
     ```

3. Structure of CSS

   - whole structure is called a ruleset, aka *rule*
   - selector: to style a different elements, change the selector , like <p>
   - properties: It specifies which of the element's properties you wanto to style. `color: red`
     - property value:  `red`

   4. Syntax of CSS

      ```
      p{
        color: red;
        width: 500px;
        border: 1px solid black;
      }
      ```

      - select multiple elements and apply one single ruleset

        ```
        p,
        li,
        h1 {
           color: red;
        }
        ```

5. CSS is all about **Box**

   - Postion: Padding, Border, Margin
     - **padding**: space around the content **内边距**
     - **border**: a solid line that is just outside of padding **边框**
     - **margin**: space around outside of border **外边距**

   - Fonts and text (typography)
     - **字体**（font-family）：选择文本的字体类型。
     
     - **字号**（font-size）：控制文本的大小。
     
     - **字重**（font-weight）：设置字体的粗细，如粗体或正常。
     
       **数值字重**：从 100 到 900 的数值，用来表示不同的粗细程度，数值越高字体越粗。例如：

       - **100** - 极细（Ultra Light）
       - **200** - 更细（Extra Light）
       - **300** - 细体（Light）
       - **400** - 正常（Normal）
       - **500** - 中等（Medium）
       - **600** - 半粗（Semi Bold）
       - **700** - 粗体（Bold）
       - **800** - 特粗（Extra Bold）
       - **900** - 超粗（Black）
     
     - **行高**（line-height）：控制行与行之间的距离。
     
     - **字间距**（letter-spacing）：控制字符之间的间距。
     
     - **文本对齐**（text-align）：控制文本的对齐方式，如居中、左对齐或右对齐。
     
     - tex shadow
     
   - Color
   
     - background color
     - text color
     - `display: block`
   
     
   
     