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

createPlot()