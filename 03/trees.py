from math import log
import operator

# 预定义的树，用来测试
def retrieveTree(i):
    listOfTree = [{'no surfacing':{ 0:'no',1:{'flippers': \
                       {0:'no',1:'yes'}}}},
                   {'no surfacing':{ 0:'no',1:{'flippers': \
                    {0:{'head':{0:'no',1:'yes'}},1:'no'}}}}
                  ]
    return listOfTree[i]

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

#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures =len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0;bestFeature = -1;
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals  = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet)
        infoGain = baseEntropy -newEntropy
        if(infoGain>bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
b = chooseBestFeatureToSplit(myDat)
# print(b)
#采用多数表决的方法决定该叶子节点的分类。
def majorityCnt(classList):
    classCount ={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return  sortedClassCount[0][0]

#创建树的函数代码
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0] == len(classList)):
        return classList[0][0]
    if len(dataSet[0])==1:
        return majorityCnt(dataSet)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    #print(bestFeat)
    bestFeatLabel = labels[bestFeat]      #最好的特征的列对应的标签
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat]for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:] #在Python语言中函数参数是列表类型时，参数是按照引用方式传递的
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree
#myTree = createTree(myDat,labels)
#print(myTree)
# 决策树分类函数
def classify(inputTree,featLabels,testVec):
    # 得到树中的第一个特征
    firstSides = list(myTree.keys())
    firstStr = firstSides[0]

    # 得到第一个对应的值
    secondDict = inputTree[firstStr]

    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        i# 如果在secondDict[key]中找到testVec[featIndex]
        if testVec[featIndex] == key:
            # 判断secondDict[key]是否为字典
            if type(secondDict[key]).__name__ == 'dict':
                # 若为字典，递归的寻找testVec
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                # 若secondDict[key]为标签值，则将secondDict[key]赋给classLabel
                classLabel = secondDict[key]
    # 返回类标签
    return classLabel

myTree = retrieveTree(1)
a = classify(myTree,labels,[1,1])
print(a)