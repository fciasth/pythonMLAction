from numpy import *
import operator
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])

    labels = ['A','A','B','B']
    return group,labels

#用于分类的输入向量inX，训练样本集dataSet，标签向量labels，用于选择最近邻的数目k；
def classify0(inX,dataSet,labels,k):
    #这一句使用到了NumPy的shape函数，返回矩阵/数组的不同维数的长度，第一个元素（shape[0]）表示第一维的长度，亦即行数
    dataSetSize  = dataSet.shape[0]
    #这里用到了NumPy中的tile(A,reps)函数，用于扩充A

    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances =sqDistances**0.5
    sortedDisIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        #这里是选择距离最小的k个点， sortedDistIndicies已经排好序，只需迭代的取前k个样本点的labels(即标签)，并计算该标签出现的次数，
        voteIlabel  = labels[sortedDisIndicies[i]]
        #还用到了dict.get(key, default=None)函数，key就是dict中的键voteIlabel，如果不存在则返回一个0并存入dict，如果存在则读取当前值并+1；
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1


    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
#测试
# group,lables = createDataSet()
# print (classify0([0,0],group,lables,3) )

#将文本函数解析成Numpy解析程序
def file2matrix(filename):
    fr  = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        lineFromLine = line.split('\t')
        returnMat[index,:] = lineFromLine[0:3]
        classLabelVector.append(int(lineFromLine[-1]))
        index +=1
    return returnMat,classLabelVector
datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')

#归一化特征值
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    #其中dataSet.min(0)中的参数0使得函数可以从列中选取最小值，而不是选取当前行的最小值。
    maxVals = dataSet.max(0)
    range1 = maxVals - minVals
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,[m,1])
    normDataSet = normDataSet/tile(range1,[m,1])
    return normDataSet,minVals,range1
#测试
normMat,minVals,range1 = autoNorm(datingDataMat)

#测试算法：作为完整程序验证分类器
def datingClassTest():
    hoRatio =0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, minVals, range1 = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print ("the classifier came back with: %d ,the real answer is: %d"%(classifierResult,datingLabels[i]))
        if(classifierResult !=datingLabels[i]): errorCount+=1.0
    print("the total error rate is: %f"%(errorCount/float(numTestVecs)))
#测试
#datingClassTest()
def classifyPerson():
    resultList = ['一点也不喜欢','有一点喜欢','很大程度喜欢']
    percentTats = float(input("玩游戏所占时间的百分比?"))
    ffMiles = float(input("每年获得的飞行常客里程数?"))
    iceCream = float(input("每周消费的冰淇淋公升数?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat,minVals,ranges1  = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr - minVals) / ranges1, normMat, datingLabels, 3)
    print("你可能喜欢这样的人:",resultList[classifierResult-1])
# 测试
# classifyPerson()

#准备数据：将图像转换为测试向量
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect
#测试
# testVector = img2vector('testDigits/0_13.txt')
# print(testVector[0,0:31])