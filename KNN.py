import operator
from numpy import *
def createDataset():
    group = array([[5.0,5.1],[4.0,4.0],[3,2.1],[0,0]])
    labels = ['A','A','B','B']
    return group,labels


#实现分类的功能，传入参数，K，group,data,要判断的点
def classify(data,group,labels,K):
    row = shape(group)[0]
    difference = (tile(data,(row,1)) - group)
    difference_Mul = (difference**2)
    distance1 = difference_Mul.sum(axis=1)
    distance2 = distance1 ** 0.5
    sortedDistance = distance2.argsort() #输出的为序号
    classCount = {}
    for i in range(K): #从0开始
        votelabel = labels[sortedDistance[i]] #第K近的label
        classCount[votelabel] = classCount.get(votelabel,0)+1 #字典为K个邻居计数，如果这个邻居的label不存在，就置零。
    result = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True) #关键字为第二个元素
    return result[0][0]



group,labels = createDataset()
#输入要判断的点，返回最可能属于哪一类
result =  classify([1.1,0.8],group,labels,3)
print(result)