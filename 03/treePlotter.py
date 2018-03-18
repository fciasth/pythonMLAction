import matplotlib.pyplot as plt

# 定义决策树决策结果的属性，用字典来定义
# 下面的字典定义也可写作 decisionNode={boxstyle:'sawtooth',fc:'0.8'}
# boxstyle为文本框的类型，sawtooth是锯齿形，fc是边框线粗细
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
# 定义决策树的叶子结点的描述属性
leafNode = dict(boxstyle="round4",fc="0.8")
# 定义决策树的箭头属性
arrow_args =dict(arrowstyle="<-")

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    # annotate是关于一个数据点的文本
    # nodeTxt为要显示的文本，centerPt为文本的中心点，箭头所在的点，parentPt为指向文本的点
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction', \
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

# 创建绘图
def createPlot():
    # 类似于Matlab的figure，定义一个画布(暂且这么称呼吧)，背景为白色
    fig = plt.figure(1, facecolor='white')
    # 把画布清空
    fig.clf()
    # createPlot.ax1为全局变量，绘制图像的句柄，subplot为定义了一个绘图，111表示figure中的图有1行1列，即1个，最后的1代表第一个图
    # frameon表示是否绘制坐标轴矩形
    createPlot.ax1 = plt.subplot(111, frameon=False)
    # 绘制结点
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    # 绘制结点
    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()

# createPlot()

#构造注解树
#获取叶节点的数目和树的层数
def getNumLeafs(myTree):
    # 定义叶节点数目
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        #判断子节点是否是字典类型
        if type(secondDict[key]).__name__=='dict':
            #递归调用
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

#获取树的层数
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth>maxDepth:
            maxDepth = thisDepth
    return maxDepth



# 预定义的树，用来测试
def retrieveTree(i):
    listOfTree = [{'no surfacing':{ 0:'no',1:{'flippers': \
                       {0:'no',1:'yes'}}}},
                   {'no surfacing':{ 0:'no',1:{'flippers': \
                    {0:{'head':{0:'no',1:'yes'}},1:'no'}}}}
                  ]
    return listOfTree[i]

#绘制中间文本
