import operator
from numpy import *

def Createdata():
    x = [[1,1],[2,2],[3,3],[4,4]]
    y = ['A','B','B','A']
    return x,y

def KNN(x,y,K,data):
    difference = x - tile(data,(shape(x)[0],1))
    difference_square = difference **2
    difference_sum = difference_square.sum(axis = 1)
    different_sum1 = difference_sum ** 0.5
    sortedDifference = sort(different_sum1)
    Dict = {}
    for i in range(k):
        labeli = y[i]
        Dict[labeli] = Dict.get(labeli,0) + 1
    sortedDict = sorted(Dict.items(),key = operator.itemgetter(1),reverse=True)
    return sortedDict[0][0]


x,y= Createdata()
k = 3
result = KNN(x,y,k,(1.5,1.5))
print(result)