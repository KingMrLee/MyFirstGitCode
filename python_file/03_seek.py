'''
seek
# 打开文件之后，从第五个字节开始读取
'''
import time

'''
with open('test01.txt', 'r', encoding='UTF-8') as f:
    # seek函数是跳过，移动一定单位之后，再打印
    f.seek(6,0)
    strChar = f.read()
    print(strChar)
'''

'''
以三个字符为单位读取文件，直到结束
'''
with open(r'test01.txt', 'r',encoding='UTF-8') as f:

    # 先从文件头开始读取3个字符，然后打印，再睡1秒，然后再继续读取
    strChar = f.read(3)
    # read读取的理解为3个汉字就是3个字符
    while strChar:
        print(strChar)
        time.sleep(1)
        strChar = f.read(3)





