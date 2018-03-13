from math import log

def calcShannonEnt(dataSet):
    #实例总数
    numEntries = len(dataSet)
    #创建了一个空字典
    labelCounts = {}

    for featVec in dataSet:
        currentLabel = featVec[-1]
        print(currentLabel)
def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no Surfacing','flippers']
    return dataSet,labels
myDat,labels = createDataSet()
calcShannonEnt(myDat)