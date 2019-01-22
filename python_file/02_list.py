'''
list创建一个列表读取文件中每一个元素
'''


with open('test01.txt','r',encoding='UTF-8') as f:
    # 将f文件作为参数传入
    l = list(f)

    for line in l:
        print(line)

# read
with open('test01.txt', 'r', encoding='UTF-8') as f1:
    # read括号中参数为读取的字符数
    strChar = f1.read(4)
    print(len(strChar))
    print(strChar)


