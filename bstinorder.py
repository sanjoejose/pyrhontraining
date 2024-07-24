class box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class box1:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
        self.root=None
        self.head=None
        self.temp=None
    def llinsert(self,data):
        nn=box1(data)
        if self.head==None:
            self.head=nn
            self.temp=nn
        else:
            self.temp.next=nn
            self.temp=
    def lltrav(self):
        t=self.head
        while t!=None:
            print(t.data)
            t=t.next
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
    def initlim(self,n1,n2):
      self.lim(self.root,n1,n2)
    def lim(self,root,n1,n2):
      if root==None:
        return
      else:
        self.lim(root.left,n1,n2)
        if root.data>=n1 and root.data<=n2:
          print(root.data,end=" ")
        self.lim(root.right,n1,n2)
l=ll()
n=int(input())
l1=list(map(int,input().split()))
for i in l1:
  l.initinsert(i)
n1=int(input())
n2=int(input())
l.initlim(n1,n2)