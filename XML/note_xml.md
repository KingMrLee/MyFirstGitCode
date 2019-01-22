# XML访问
## 读取
- xml读取的两个主要技术：SAX、DOM
    - SAX（Simple API for XML）
        - 基于事件驱动的API
        - 利用SAX解析文档涉及到解析器和事件处理两部分
        - 特点：    
            - 快
            - 流式读取
    - DOM 
        - 是w3c规定的XML编程接口
        - 一个XML文件在缓存中以树形结构保存，存取
        - 添加删除相关案例
        - minidom
            - minidom.parse(filename)                     #加载和读取xml文件
            - doc.documentElement                         #获取xml文档对象
            - node.getAttribute(AttributeName)            #获取xml节点属性值
            - node.getElementsByTagName(TagName)          #获取xml节点对象集合
            - node.childNodes                             #获取子节点列表
            - node.childNodes[index].nodeValue        #获取xml节点值
            - node.firstChild                             #访问第一个节点
            - n.childNodes[0].data                        #获得文本值
            - node.childNodes[index].nodeValue        #获取XML节点值

        - etree