import numpy as np, pandas as pd, math

data = pd.read_csv(r'C:\Users\HP\Desktop\duoyuanlunwen\data_xiugai.csv')
print(data)
new_data = data.iloc[:, 2:].values     #将DataFrame变为列表，每行为一组

def eucliDist(A, B):
    return math.sqrt(sum([(a - b) ** 2 for (a, b) in zip(A, B)]))

def k_means(c, data, max,label):
    # a. 输入质心列表c，待聚类数据`data`，最大迭代次数max
    max = max - 1
    num = len(data)
    # b. 计算data中的每个点分到k个质心的距离，得到一个矩阵，如
    metrix = [[eucliDist(a, b) for a in data] for b in c]
    print(metrix)
    # c. 比较矩阵同一列的数值大小，将对应的学生划归距离较短的质心所属的类，将标签存储为列表
    classifier = []
    for (d, e, f) in zip(metrix[0], metrix[1], metrix[2]):
        m = min(d, e, f)
        if d == m:
            classifier.append(label[0])
        elif e == m:
            classifier.append(label[1])
        else:
            classifier.append(label[2])

    print(classifier)

    # d. 重新计算质心的坐标，新质心的坐标=被划归同一类点的坐标的平均值
    n1, n2 = 0, 0
    c1 = [0, 0, 0, 0, 0]
    c2 = c1
    c3 = c1
    for i in range(0, num):

        if classifier[i] == label[0]:
            c1 = [a + b for (a, b) in zip(c1, data[i])]
            n1 = n1 + 1
        elif classifier[i] == label[1]:
            c2 = [a + b for (a, b) in zip(c2, data[i])]
            n2 = n2 + 1
        else:
            c3 = [a + b for (a, b) in zip(c3, data[i])]

    c1 = [a / n1 for a in c1]
    c2 = [a / n2 for a in c2]
    c3 = [a / (num - n1 - n2) for a in c3]

    print(max)
    print([c1,c2,c3])
    # e. 重复b~d，直到质心坐标不再变化,或达到最大迭代次数
    if c != [c1, c2, c3] and max > 0:

        c = [c1, c2, c3]
        print(c)
        k_means(c, data, max, label)
    return classifier


c = [
[ 421314, 120872, 4092, 364723, 18608, 92094, 1350],
[2027900 ,  387400,   128000, 1520600,  565100,   88700 ,  20800],
[ 252523,  158709,   22551 , 151117,    7120,  143486 ,  22211]]
label = ['A', 'B', 'C']
max = 20

print(k_means(c, new_data, max, label))

lei = pd.DataFrame(k_means(c, new_data, max, label))
lei.names = '类'
print(data)
print(lei)

result = pd.concat([data, lei], axis=1)

#jieguo = pd.join(data, lei, how='inner')

result = result.sort_values(by = 0)
print(result)

result.to_csv(r'C:\Users\HP\Desktop\duoyuanlunwen\result.csv', index=False, encoding='UTF8')#写入数据

ser = result[['县(市)名称', 0]]
print(ser)

ser.to_csv(r'C:\Users\HP\Desktop\duoyuanlunwen\ser.csv', index=False, encoding='UTF8')#写入数据



