import pandas as pd
import numpy as np
data = pd.read_csv(r'C:\Users\HP\Desktop\duoyuanlunwen\data.csv', index_col = 'ID')
print(data)
data['县(市)代码'] = data['县(市)代码'].astype('str')
a = []
for i in data['县(市)代码'].values.tolist():
    if '00' in i:
        a.append(data['县(市)代码'].values.tolist().index(i))
print(a)
data = data.drop(data.index[a])
data = data.reset_index(drop = True)
print(data)
data = data.drop('总和', axis = 1)
jishu = (data == 0).astype(int).sum(axis=0)#计算每一列0的个数，返回一个Series
jishushaixuan = jishu[jishu < 10] # 起取缺失值小于10的列
data = data[list(jishushaixuan.index)]
data = data.drop('数据年份', axis = 1)#删除与分类无关的列
print(data)#查看数据
data.to_csv(r'C:\Users\HP\Desktop\duoyuanlunwen\data_xiugai.csv', index=False, encoding='UTF8')#写入数据


