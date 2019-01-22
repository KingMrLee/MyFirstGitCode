# -*- coding:utf-8 -*-
#conding:utf-8
__author__ = 'hdfs'
'''
简洁 高效 明了
ElementTree轻量级的 Python 式的 API ，
它由一个 C 实现来提供。
相对于 DOM 来说，
ET 快了很多(见注释3)而且有很多令人愉悦的 API 可以使用。
相对于 SAX 来说，ET 也有 ET.iterparse 提供了 “在空中” 的处理方式，
没有必要加载整个文档到内存。
ET 的性能的平均值和 SAX 差不多
'''
import pprint
from xml.etree.ElementTree import parse
mapping={}
#获取解析树
tree=parse("bools.xml")
#找到所有的book节点
for B in tree.findall('book'):
    #获取属性
    isbn=B.attrib['isbn']
    #找到该节点下的所有子节点为title的界定啊
    for T in B.findall('title'):
        #获取数据文本
        mapping[isbn]=T.text

pprint.pprint(mapping)