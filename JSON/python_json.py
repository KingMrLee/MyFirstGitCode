import json

test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
print(test_dict)
print(type(test_dict))
# dumps 将数据转换成字符串 对数据编码，把python格式表示成json格式
json_str = json.dumps(test_dict)
print(json_str)
print(type(json_str))

# loads 将字符串转换为字典 对数据解码，把json格式转换成python格式
new_dict = json.loads(json_str)
print(new_dict)
print(type(new_dict))


# 将数据写入json文件中
with open("config/record.json","w") as f:
    json.dump(new_dict,f)
    print("加载入文件完成...")



# 把文件打开，并把字符串变换为数据类型
with open(r"config/record.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
print(load_dict)

with open(r"config/record.json","w") as dump_f:
    json.dump(load_dict,dump_f)

