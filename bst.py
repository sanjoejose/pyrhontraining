class box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class ll:
    def __init__(self):
        self.root=None
    def initinsert(self,data):
        nn=box(data)
        self.insert(self.root,nn)
    def inittrav(self):
        self.trav(self.root)
    def insert(self,temp,nn):
        if self.root==None:
            self.root=nn
            return
        elif (nn.data<temp.data):
            if temp.left==None:
                temp.left=nn
            else:
                self.insert(temp.left,nn)
        else:
            if temp.right==None:
                temp.right=nn
            else:
                self.insert(temp.right,nn)
    def trav(self,root):
        if root==None:
            return
        else:
            print(root.data,":",sep="",end="")
            if root.left!=None:
                print("L:",root.left.data,",",sep="",end="")
            if root.right!=None:
                print("R:",root.right.data,sep="",end="")
            print()
            self.trav(root.left)
            self.trav(root.right)
    def search(self,key):
        t=self.initsearch(self.root,key)
        if t==1:
            print("true")
        else:
            print("false")
    def rem(self,key,root):
        if root==None:
            return
        else:
            if key>root.data:
                self.rem(key,root.right)
            elif key<root.data:
                self.rem(key,root.left)
            elif key==root.data:
                if root
    def initsearch(self,temp,key):
        if temp==None:
            return -1
        else:
            if temp.data==key:
                return 1
            else:
                if key>temp.data:
                    t=self.initsearch(temp.right,key)
                    return t
                else:
                    t=self.initsearch(temp.left,key)
                    return t
l=ll()
n=int(input())
list1=list(map(int,input().split()))
for i in list1:
    l.initinsert(i)
n=int(input())
l.search(n)