'''
文件操作
'''
'''
# 打开文件，用写的方式
# r表示后面字符串内容不需要转义
# 当前目录下之前没有test01.txt，但是执行代码之后，写方式默认会自动创建一个文件test01.txt
f = open("test01.txt",'w')
# 文件打开后必须关闭
f.close()


with语句案例

# 案例1
with open(r"test01.txt",'r') as f:
    pass
    # 下面语句块开始对文件f进行操作
    # 在本模块不需要再使用close语句关闭文件f

'''
# 案例2
with open('test01.txt', 'r',encoding='UTF-8') as f:
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够正确按行读取文件直到结束
    while strline:
        print(strline)
        # 再读一行
        strline = f.readline()