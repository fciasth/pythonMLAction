from math import log

def calcShannonEnt(dataSet):
    #实例总数
    numEntries = len(dataSet)
    #创建了一个空字典
    labelCounts = {}

    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

def createDataSet():
    dataSet = [[1,1,'maybe'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no Surfacing','flippers']
    return dataSet,labels
# myDat,labels = createDataSet()
# a= calcShannonEnt(myDat)
# print(a)

#划分数据集
