dic = {1:'a',2:'b',3:'C'}
dic2 = {4:'d',5:'e',6:'F'}
print(dic.get(1))
print(dic.values())
print(dic.keys())
print(dic.items())
print(dic.pop(1))
print(dic)
print(dic.popitem())
print(dic)
dic.update(dic2)
print(dic)
dic1 = dic.copy()
print(dic1)
dic1[7]='g'
print(dic1)
for k,v in dic.items():
    print(k,":",v)
# dict1 = {}
# n = eval(input("enter the range:"))
# for i in range(n):
#     k = input("enter the key:")
#     v = input("enter the values:")
#     dict1[k] = v
# print(dict1)