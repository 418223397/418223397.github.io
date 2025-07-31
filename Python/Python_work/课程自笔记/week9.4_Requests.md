### Requests:

- 基本的get,post的用法

- get 如何携带请求参数 params

  ```
  >>> payload = {'key1': 'value1', 'key2': 'value2'}
  >>> r = requests.get("http://httpbin.org/get", params=payload)
  ```

  

- post 如何携带请求参数data\json

  ```
  >>> payload = {'key1': 'value1', 'key2': 'value2'}
  
  >>> r = requests.post("http://httpbin.org/post", data=payload)
  ```

  

- 将json格式的数据请求到后端接口api

  ```
  >>> import json
  
  >>> url = 'https://api.github.com/some/endpoint'
  >>> payload = {'some': 'data'}
  
  >>> r = requests.post(url, data=json.dumps(payload))
  >>> url = 'https://api.github.com/some/endpoint'
  >>> payload = {'some': 'data'}
  
  >>> r = requests.post(url, json=payload)
  ```

  

- cookie

  ```
  >>> url = 'http://httpbin.org/cookies'
  >>> cookies = dict(cookies_are='working')
  
  >>> r = requests.get(url, cookies=cookies)
  ```

  

- session

  ```
  s = requests.Session()
  
  s.get('https://httpbin.org/cookies/set/sessioncookie/123456789', cookies=cookies)
  r = s.get('https://httpbin.org/cookies')
  ```

  

### BeautifulSoup4

- 基本获取元素的方式：
  - find()
  - find_all()
  - 筛选标签：find('a', class_='mayugu')



### 

### 提速爬虫-利用线程或进程

1. 线程池提速爬虫
2. 进程池提速爬虫