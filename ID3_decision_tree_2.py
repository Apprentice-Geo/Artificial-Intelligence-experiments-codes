import copy
import math
import numpy as np
import matplotlib.patches as pat
import matplotlib.pyplot as plt


def d_rect(x,y,r,c,s):#(x,y)最上面边的中点坐标，r长度的???（根据想要的相对大小设置），c宽
    r*=2.8
    plt.plot((x-r,x+r),(y,y),ls='-',color='#00FFFF')
    plt.plot((x+r, x+r), (y, y-c),ls='-',color='#00FFFF')
    plt.plot((x-r, x-r), (y, y-c),ls='-',color='#00FFFF')
    plt.plot((x-r, x+r), (y-c, y-c),ls='-',color='#00FFFF')
    plt.text(x-19*r/20,y-2*c/3,s)

class DataSet:
    def __init__(self, data):
        self.data = []
        self.labeldata = {}
        self.split = {}
        if len(data)==0:return
        for line in data:
            self.data.append(list(float(x) for x in line))
            self.data[len(self.data) - 1][-1] = int(self.data[len(self.data) - 1][-1])
            if self.data[len(self.data) - 1][-1] not in self.labeldata:
                self.labeldata[self.data[len(self.data) - 1][-1]] = [self.data[len(self.data) - 1]]
            else:
                self.labeldata[self.data[len(self.data) - 1][-1]].append(self.data[len(self.data) - 1])
        for i in range(len(self.data[0]) - 1):
            self.split[i] = (0, 0)
        tmpdata = copy.deepcopy(self.data)
        for i in self.split.keys():
            tmpdata.sort(key=lambda x: x[i])
            for j in range(len(tmpdata) - 1):
                A = []
                tmpdic = {}
                for k in tmpdata[:j + 1]:
                    if k[-1] not in tmpdic:
                        tmpdic[k[-1]] = [k]
                    else:
                        tmpdic[k[-1]].append(k)
                A.append(tmpdic)
                tmpdic = {}
                for k in tmpdata[j + 1:]:
                    if k[-1] not in tmpdic:
                        tmpdic[k[-1]] = [k]
                    else:
                        tmpdic[k[-1]].append(k)
                A.append(tmpdic)
                self.split[i] = max(
                    (self.split[i], (self.infoD_A(self.labeldata, A), (tmpdata[j][i] + tmpdata[j + 1][i]) / 2)),
                    key=lambda x: x[0])

    # D是字典
    def infoD(self, D):
        r = 0
        total = 0
        for item in D.values():
            total += len(item)
        for item in D.values():
            r += -(len(item) / total) * math.log2(len(item) / total)
        return r

    # A是元素为字典的数组
    def infoD_A(self, D, A):
        r = self.infoD(D)
        total = 0
        typecnt = []
        for item in D.values():
            total += len(item)
        for i in range(len(A)):
            typecnt.append(0)
            for key, item in A[i].items():
                typecnt[i] += len(item)
            r -= self.infoD(A[i]) * typecnt[i] / total
        return r

    def show(self):
        print(self.data)
        for key, item in self.labeldata.items():
            print(key, end=': ')
            print(item)
        for key, item in self.split.items():
            print(key, end=': ')
            print(item)


class TreeNode:
    def __init__(self, dataSet, d):
        self.Maxdeep = 6
        self.deep = d + 1
        self.h=0
        self.labeldata = dataSet.labeldata
        self.type = None
        self.t = 0  # 0node,1leaf
        self.dKey = -1
        self.dValue = float('inf')
        self.dGain = 0
        self.lData = []
        self.rData = []
        self.l = None
        self.r = None
        if len(self.labeldata) == 1:
            self.t = 1
            for i in self.labeldata.keys():
                self.type = i
            return
        if self.deep == self.Maxdeep:
            tmp = 0
            self.t = 1
            for key, item in self.labeldata.items():
                if len(item) >= tmp:
                    self.type = key
                    tmp = len(item)
            return
        for key, item in dataSet.split.items():
            if item[0] > self.dGain:
                self.dKey = key
                self.dValue = item[1]
                self.dGain = item[0]
        for i in range(len(dataSet.data)):
            if dataSet.data[i][self.dKey] <= self.dValue:
                self.lData.append(dataSet.data[i])
            else:
                self.rData.append(dataSet.data[i])
        self.rData = DataSet(self.rData)
        self.lData = DataSet(self.lData)
        if len(self.lData.data)==0 or len(self.rData.data) ==0:
            tmp = 0
            self.t = 1
            for key, item in self.labeldata.items():
                if len(item) >= tmp:
                    self.type = key
                    tmp = len(item)
            return
        if len(self.rData.data) > 0:
            self.r = TreeNode(self.rData, self.deep,)
        if len(self.lData.data) > 0:

            self.l = TreeNode(self.lData, self.deep)
        self.priOrder()
    def priOrder(self):
        if self is None:
            return 0
        lh=0
        rh=0
        if self.l is not None:
            lh=self.l.priOrder()
        if self.r is not None:
            rh=self.r.priOrder()
        self.h = max(lh, rh) + 1
        return self.h
    def test(self, data):
        if self.t == 1:
            return self.type
        if data[self.dKey] <= self.dValue:
            return self.l.test(data)
        else:
            return self.r.test(data)

    def draw(self):
        _,ax=plt.subplots()
        plt.title('ID3_Decision_Tree', fontsize=15)
        R=100
        C=150
        CirR = C/2
        maxX=0
        minX=float('inf')
        maxY=0
        minY=float('inf')
        X=1/2*4*R*(2**(self.h-1))
        Y=2*C*(self.h+2)
        xChange=3*R
        ychange=2*C
        maxY=Y
        ls=[(self,X,Y,R,C)]
        while len(ls)>0:
            tmp,x,y,r,c=ls.pop(0)
            if tmp.t==0:
                d_rect(x,y,r,c,"Key:%d,Value:%.3f"%(tmp.dKey,tmp.dValue))
                if tmp.l is not None:
                    minX=min(minX,x-xChange)
                    minY=min(minY,y-ychange)
                    plt.plot((x,x-xChange),(y-c,y-ychange),color="#FF4040",ls='-')
                    ls.append((tmp.l,x-xChange,y-ychange,r,c))
                if tmp.r is not None:
                    maxX=max(maxX,x+xChange)
                    minY = min(minY, y - ychange)
                    plt.plot((x,x+xChange),(y-c,y-ychange),color="#FF4040",ls='-')
                    ls.append((tmp.r,x+xChange,y-ychange,r,c))
            else:
                ax.add_artist(pat.Circle((x,y-CirR),CirR,color="#00FF7F"))
                plt.text(x-CirR,y-3*CirR,"Type:%d"%tmp.type)
        plt.xlim((minX-xChange,maxX+xChange))
        #plt.xticks(np.arange(minX-xChange,maxX+xChange,(maxX-minX+2*xChange)/10))
        plt.xticks([])
        plt.ylim((minY-2*ychange, maxY+ychange))
        #plt.yticks(np.arange(minY-2*ychange, maxY+ychange,(maxX-minX+2*xChange)/10))
        plt.yticks([])
        plt.show()
if __name__ == "__main__":
    path = "traindata.txt"
    lines = None
    with open(path, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].split()
    traindatas = DataSet(lines)
    #traindatas.show()
    Tree = TreeNode(traindatas, -1)
    testPath="testdata.txt"
    with open(testPath, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].split()
    testdatas = DataSet(lines)
    error=[]
    for data in testdatas.data:
        r=Tree.test(data)
        if r!=data[-1]:
            error.append((data,r))
    print("误分类：")
    for i in error:
        print("数据：",end=' ')
        print(i[0],end=' ')
        print("误分类为：%d"%i[1])
    print("准确率：%.3f"%(1-len(error)/len(testdatas.data)))
    Tree.draw()