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



# createPlot()

#构造注解树
#获取叶节点的数目和树的层数
def getNumLeafs(myTree):
    # 定义叶节点数目
    numLeafs = 0
    firstSides = list(myTree.keys())
    firstStr = firstSides[0]
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
    firstSides = list(myTree.keys())
    firstStr = firstSides[0]
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
def plotMidText(cntrPt,parentPt,txtString):
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
    #text函数为 matplotlib的函数 用于显示文本
    createPlot.ax1.text(xMid,yMid,txtString)

#绘制决策树
def plotTree(myTree,parentPt,nodeTxt):
    numLeafs =getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    # 得到第一个特征
    firstSides = list(myTree.keys())
    firstStr = firstSides[0]
    # 计算坐标，x坐标为当前树的叶子结点数目除以整个树的叶子结点数再除以2，y为起点
    cntrPt = (plotTree.xOff+(1.0+float(numLeafs))/2.0/plotTree.totalW,plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)

    plotNode(firstStr,cntrPt,parentPt,decisionNode)
    # 根据firstStr找到对应的值
    secondDict = myTree[firstStr]
    # 因为进入了下一层，所以y的坐标要变 ，图像坐标是从左上角为原点
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    # 遍历secondDict
    for key in secondDict.keys():
        # 如果secondDict[key]为一棵子决策树，即字典
        if type(secondDict[key]).__name__ == 'dict':
            # 递归的绘制决策树
            plotTree(secondDict[key], cntrPt, str(key))
            # 若secondDict[key]为叶子结点
        else:
            # 计算叶子结点的横坐标
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            # 绘制叶子结点
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            # 这句注释掉也不影响决策树的绘制,自己理解的浅陋了，这行代码是特征的值
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
            # 计算纵坐标
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD

# 创建绘图
def createPlot(inTree):
    # 类似于Matlab的figure，定义一个画布(暂且这么称呼吧)，背景为白色
    fig = plt.figure(1, facecolor='white')
    # 把画布清空
    fig.clf()
    # createPlot.ax1为全局变量，绘制图像的句柄，subplot为定义了一个绘图，111表示figure中的图有1行1列，即1个，最后的1代表第一个图
    # frameon表示是否绘制坐标轴矩形
    # 定义横纵坐标轴，无内容
    axprops =dict(xticks=[],yticks=[])
    # 绘制图像，无边框，无坐标轴
    createPlot.ax1 = plt.subplot(111, frameon=False,**axprops)
    # plotTree.totalW保存的是树的宽
    plotTree.totalW = float(getNumLeafs(inTree))
    # plotTree.totalD保存的是树的高
    plotTree.totalD = float(getTreeDepth(inTree))
    # 决策树起始横坐标
    plotTree.xOff = -0.5/plotTree.totalW;
    plotTree.yOff = 1.0;
    plotTree(inTree,(0.5,1.0),'')
    plt.show()

myTree = retrieveTree(0)
createPlot(myTree)