'''
持久化-shelve
'''
import shelve
'''
# 运行之后可以看到，shelve自动创建的不仅仅是一个shv.db文件，还包括一些其他格式的文件
shv = shelve.open(r'shv.db')

shv['one'] = 1
shv['two'] = 2
shv['three'] = 3

shv.close()

# shelve 的读取案例
shv2 = shelve.open(r'shv.db')
try:
    print(shv2['one'])
    print(shv2['threee'])
except Exception as e:
    print("你好烦啊")
finally:
    shv2.close()

# shelve强制写回案例，加上参数writeback=True

shv3 = shelve.open(r'shv.db',writeback=True)
try:
    print(shv3['one'])
    shv3['one'] = 999
    k1 = shv3['one']
    print(k1)
except Exception as e:
    print("Unknow Error")
finally:
    shv3.close()

shv4 = shelve.open(r'shv.db')
try:
    k2 = shv4['one']
    print(k2)
except Exception as e:
    print("Unknow Error")
finally:
    shv4.close()
'''
# shevle 使用with管理上细纹环境

with shelve.open(r'shv.db',writeback=True) as shv:
    print(shv['one'])
    shv['one'] = {"eins":1,"zewei":2,"threee":3}
    k_shv1 = shv['one']
    print(k_shv1)
    k_shv1["eins"] = 1000

with shelve.open(r'shv.db') as shv2:
    print(shv2['one'])