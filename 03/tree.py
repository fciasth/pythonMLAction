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
myDat,labels = createDataSet()
# a= calcShannonEnt(myDat)
# print(a)

#划分数据集
#三个输入参数：待划分的数据集、划分数据集的特征、需要返回的特征的值
def splitDataSet(dataSet,axis,value):
    # Python语言不用考虑内存分配问题。 Python语言在函数中传递的是列表的引用，
    # 在函数内部对列表对象的修改，将会影响该列表对象的整个生存周期。为了消除这
    # 个不良影响，我们需要在函数的开始声明一个新列表对象。
    retDataSet = []
    for featVec in dataSet:
       # print(featVec[axis])
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            # a[2:4]  从第2个元素开始，到第4个为止的元素。包括头不包括尾。
            reducedFeatVec.extend(featVec[axis+1:])

            #上面两行就是把作为特征的一列去掉了
            retDataSet.append(reducedFeatVec)
    return retDataSet
a= splitDataSet(myDat,2,"no")
#print(a)