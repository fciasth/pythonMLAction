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

#归一化特征值
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    range = maxVals - minVals

# group,lables = createDataSet()
# print (classify0([0,0],group,lables,3) )