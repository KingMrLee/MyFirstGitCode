# 解析案例
from xml.dom import minidom

doc = minidom.parse('test.xml')  # parse("foo.xml")
# parseString("<foo><bar/></foo>")

# 实例化
root = doc.documentElement  # 注意没括号

# 文档对象元素
print ('--' * 25)
print (root.nodeName)  # 节点名字，collection
print (root.nodeValue)  # 节点的值，None
print (root.nodeType)  # 节点类型，1
print (root.ELEMENT_NODE)  # 1
print ('--' * 25)

# 在集合中获取所有电影
nodes = root.getElementsByTagName('movie')  # 获取xml节点对象集合

# 打印每部电影的详细信息
for n in nodes:
    # print n#<DOM Element: movie at 0x1f9d968>

    # 获得电影的title的属性值
    # print n.getAttribute('title')

    # 获取xml节点type对象的具体信息
    type = n.getElementsByTagName('type')[0]
    print ("Type:%s" % type.childNodes[0].data)  ##获得文本值