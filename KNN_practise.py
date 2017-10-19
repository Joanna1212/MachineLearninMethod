import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def file2matrix(filename,col):
    fr = open(filename)
    arrayLine = fr.readlines() 
    numLine = len(arrayLine) #得到文件行数
    returnMat = np.zeros((numLine, col)) #create the return matrix
    classLabelVector = []
    index = 0
    for line in arrayLine:
        line = line.strip() #remove the empty from the left and right
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:col]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

def normalization(x):
    minVals = x.min(0) #axis = 0 refers to the smallest number of each column
    maxVals = x.max(0)
    ranges = maxVals - minVals
    normX = np.zeros(np.shape(x))
    row = x.shape[0]
    normX = x - np.tile(minVals,(row,1))
    normX = normX / np.tile(range,(row,1))
    return normX, ranges, minVals #return ranges and minVals to normalize testing data

x,y = file2matrix('datingTestSet.txt',3)
fig = plt.figure()
ax = fig.add_subplot(111)  #one row one col and at the first block of the figure.
ax.scatter(x[:,1],x[:,2],50.0*np.array(y),100.0*np.array(y))
print(x[:,1])
plt.show()
