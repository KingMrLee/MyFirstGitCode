'''
tell
- 每读取三个字符，打印出当前读取指针的位置，然后继续读取
'''
import time
with open(r'test01.txt', 'r', encoding='UTF-8') as f:

    strChar = f.read(3)
    pos = f.tell()

    while strChar:
        print(pos)
        print(strChar)
        time.sleep(1)
        strChar = f.read(3)
        pos = f.tell()