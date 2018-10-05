# import pickle
# #将变量序列化并写入文件
# d=dict(name='Bob',age=12,score=88)
# f=open('.\\dump.txt','wb')
# pickle.dump(d,f)
# f.close()
#
# #将序列化从文件中读出
# f=open('.\\dump.txt','rb')
# d=pickle.load(f)
# f.close()
# print(d)
import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)