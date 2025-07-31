HTML Basics

1. Definition: Hyper Text Makeup Language that defines the structures of the content.

2. Role: HTML consist of a series of **elements**, which you use to enclose, or wrap, different parts of the content to make it appear a certain way, or act a certain way. The enclosing **tags** can make a word or image hyperlink to somewhere else, can italicize words, can make the font bigger or smaller, and so on. 

   - Main Elements as follows:
     - Paragraph
     - List
     - Heading
     - Links
     - images
     - multimedia player
     - forms
     - self-defined

3. 4 main parts in element:

   - opening tag: <p>
   - closing tag: </p> (forward slash before the element name)
   - content 
   - element

4. Elements have attributes

   - Attributes contain extra information about the element that you don't want to appear in the actual content. 

     ```html
     <p class="editor-note">
         My Cat is very grumpy
     </p>
     ```

     `class`: attribute name

     `editor-note`: the attribute value

     - Some attributes have no value, such as `required`

   - Nesting elements: put elements inside other elements

     ```html
     <p>
         My cat is <strong>very</strong>grump.
     </p>
     ```

- - Void elements: some elements have no content

    ```html
    <img src="images/firefox-icon.png" alt="My test image" />
    
    ```

    - The content has two attributes, no closing `</img>` and no inner content
    - Coz an image element doesn't wrap content to affect it. Its purpose to embed an image in the HTML page in the place it appears. 

5. Anatomy of an HTML document

   ```html
   <!doctype html> #文档类型声明， <!-- and -->is an HTML COMMENT
   <html lang="en-US">
     <head>
       <meta charset="utf-8" />
       <meta name="viewport" content="width=device-width" />
       <title>My test page</title>
     </head>
     <body>
       <img src="images/firefox-icon.png" alt="My test image" />
     </body>
   </html>
   ```

   - Heading: <h1>-<h6>

   - Paragraphs: <p>--</p>

   - List

     - Unordered list: <ul>
     - Ordered list: <ol>
     - item inside the lists: <li>

     ```html
     
     <p>
         At Mozilla, we're a global <strong>community</strong>of</p>
     <ul>
         <li>technologists</li>
         <li>thinkers</li>
         <li>buliders</li>
     </ul>
     
     ```



- - Links

    ```html
    <a href="http://github.com/fatbookpro">Mozilla Manifesto</a>
    ```

    

Terms:

- src: source

- alt: alternative

- href: hyper reference

