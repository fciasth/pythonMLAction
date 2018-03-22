from numpy import *
######
#优秀文档http://blog.csdn.net/kevinelstri/article/details/52268566
######
#创建实验样本，真实样本可能差很多，需要对真实样本做一些处理，比如
#去停用词(stopwords)，词干化(stemming)等等，处理完后得到更"clear"的数据集，方便后续处理


def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1代表存在侮辱性的文字，0代表不存在
    return postingList,classVec

def createVocabList(dataSet):
    # 将所有文档所有（去重的）词都存到一个列表中，可用set()函数去重。
    # 用上set()函数操作符号|，取并集，或者写两重循环用vocabSet.add()
    vocabSet = set([])
    # return list(set([word for doc in dataSet for word in doc])
    # [word for doc in dataSet for word in doc]: 用列表推导式将dataSet转为1维列表，
    # set(XXX)： 将这个列表去重转为集合
    # list(set(XXX)): 又转回来

    for document in dataSet:
        vocabSet = vocabSet | set(document)

    return  list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):#输入参数为词汇表及某个文档
    returnVec = [0]*len(vocabList)#首先创建一个和词汇表等长的向量，并将其元素都设置为0
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!"%word)
    return returnVec
# dataSet,classVec = loadDataSet()
# print(createVocabList(dataSet))
listOPosts,listClasses = loadDataSet()
myVocabList = createVocabList(listOPosts)
# print (myVocabList) #在输出的这个此表中，不会出现重复的词
# print ("\n")
#
# Vec = setOfWords2Vec(myVocabList, listOPosts[5])
# print (Vec)

# 条件概率的计算
def trainNB0(trainMatrix,trainCategory):  #输入为文档矩阵及对应的标签向量
    numTrainDocs = len(trainMatrix) #文档数
    numWords = len(trainMatrix[0])  #词汇表长度
    pAbusive = sum(trainCategory)/float(numTrainDocs) #属于侮辱性文档的概率
    p0Num = ones(numWords); p1Num = ones(numWords)      #长度为词汇表大小的0向量
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:   #如果第i个文档是侮辱性文档
            p1Num += trainMatrix[i] #所有侮辱性文档词向量累加，每个分量就是该词的频数
            p1Denom += sum(trainMatrix[i])  # 所有侮辱性文档 词总数
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom #向量除以浮点数
    p0Vect = p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive

trainMat = []
for postinDoc in listOPosts:
    trainMat.append(setOfWords2Vec(myVocabList, postinDoc))

p0v,p1v,pAb =trainNB0(array(trainMat),array(listClasses))
# print(p0v)

def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1 = sum(vec2Classify*p1Vec) + log(pClass1)
    p0 = sum(vec2Classify*p0Vec) + log(1.0-pClass1)
    if p1>p0:
        return 1
    else:
        return 0

def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
testingNB()

def bagOfWord2VecMN(vocabList,inputSet):
    returnVect = [0]*len(vocabList)
    for word in inputSet:
        returnVect[vocabList.index(word)] +=1
    return returnVect