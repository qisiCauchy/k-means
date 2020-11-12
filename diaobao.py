#-*-coding = utf-8 -*-
#@Time:  16:28
#@AUTHER: 张鹏程
#@File：diaobao.py
#@Software: PyCharm

data = pd.read_csv(r'C:\Users\HP\Desktop\duoyuanlunwen\data_xiugai.csv')
print(data)
new_data = data.iloc[:, 2:].values     #将DataFrame变为列表，每行为一组


grade = k_means(c, new_data, max, label)
grade = pd.Series(grade, index=data['学生姓名'])
print(grade)