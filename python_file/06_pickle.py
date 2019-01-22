'''
序列化案例
'''

import pickle

# 简单案例
age = 23
a1 = ['24','I love heyuyu',['guoleilei','shazi']]

with open(r'test01.txt','wb') as f:
    pickle.dump(a1,f)

# 这里可以看出来pickle可以把复杂的二级list也可以写进去和读取出来
with open(r'test01.txt','rb') as f2:
    a2 = pickle.load(f2)
    print(a2)