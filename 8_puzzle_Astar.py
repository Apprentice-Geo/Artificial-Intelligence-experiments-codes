import copy
import heapq
def inv(ls):
    re=0
    for i in range(len(ls)):
        if ls[i]==0:
            continue
        for j in range(i):
            if ls[j]>ls[i]:
                re+=1
    return re

class gh:
    def __init__(self,ls):
        self.cur=ls
        self.z=self.findx(0)
        self.pre=None
        self.d=0
        self.aim=[[1,2,3],[8,0,4],[7,6,5]]
        self.h=self.getH()
        self.f=self.d+self.h
    def __lt__(self,other):
        return self.f<other.f
    def findx(self,x):
        for i in range(3):
            for j in range(3):
                if self.cur[i][j]==x:
                    return i,j
    def deep(self):
        if self.pre is not None:
            self.d=self.pre.d+1
        else:
            self.d=0
    def getH(self):
        H=0
        for i in range(3):
            for j in range(3):
                x,y=self.findx(self.aim[i][j])
                H+=abs(x-i)+abs(y-j)
        return H
    def refresh(self):
        self.deep()
        self.h=self.getH()
        self.f = self.d + self.h

    def mover(self,r):#row
        x=self.z[0]+r
        y=self.z[1]
        if x>2 or x<0:
            return None
        Copy=copy.deepcopy(self)
        Copy.pre = self
        tmp=Copy.cur[x][y]
        Copy.cur[x][y]=0
        Copy.cur[x-r][y]=tmp
        Copy.z=(x,y)
        Copy.refresh()
        return Copy

    def movec(self,c):#column
        x = self.z[0]
        y = self.z[1]+c
        if y > 2 or y < 0:
            return None
        Copy = copy.deepcopy(self)
        Copy.pre=self
        tmp = Copy.cur[x][y]
        Copy.cur[x][y] = 0
        Copy.cur[x][y-c] = tmp
        Copy.z = (x, y)
        Copy.refresh()
        return Copy

    def getNewCur(self):
        curs=[]
        curs.append(self.movec(1))
        curs.append(self.movec(-1))
        curs.append(self.mover(1))
        curs.append(self.mover(-1))
        i=0
        while i<len(curs):
            if curs[i] is None:
                del curs[i]
            else:
                i+=1
        return curs


    def test(self):
        curls=[]
        aimls=[]
        for i in range(3):
            curls.extend(self.cur[i])
            aimls.extend(self.aim[i])
        C=inv(curls)
        A=inv(aimls)
        if C%2!=A%2:
            return False
        else:
            return True
    def hash(self):
        re = 0
        curls = []
        for i in range(3):
            curls.extend(self.cur[i])
        for i in range(9):
            re+=curls[i]*9**i
        return re
    def show(self):
        if self.pre is not None:
            self.pre.show()
        for i in range(3):
            print(self.cur[i])
        print("deep: %d"%self.d)
        print("h: %d" % self.h)
        print("-------------------------------------------")

def Astar(ls):
    g=gh(ls)
    if g.test() is False:
        print("there is no answer")
        return
    que=[]
    Set = set()
    Set.add(g.hash())
    heapq.heapify(que)
    que.append(g)
    tmp=heapq.heappop(que)
    while tmp.h!=0:
        Newcur=tmp.getNewCur()
        for Cur in Newcur:
            if Cur.hash() not in Set:
                Set.add(Cur.hash())
                heapq.heappush(que,Cur)
        tmp=heapq.heappop(que)
    return tmp

if __name__ =="__main__":
    ls=[]
    for i in range(3):
        ls.append(list(map(int,input().split())))
    ans=Astar(ls)
    if ans is not None:
        ans.show()






