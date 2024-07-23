class box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class qu:
    def __init__(self):
        self.que=[[0]]*100
        self.front=-1
        self.rear=-1
    def push(self,data):
        if self.front==-1:
           self.front+=1
           self.rear+=1
           self.que[self.rear]=data
        else:
            self.rear+=1
            self.que[self.rear]=data
    def res(self):
        self.co=self.front
    def pop(self):
      if self.co>self.rear or self.front==-1:
        return -1
      else:
        t=self.que[self.co]
        self.co+=1
        return t
class ll:
    def __init__(self):
        self.root=None
        self.q=qu()
    def intrav(self):
        t=self.inorder(self.root)
        if t==1:
          print("True")
        else:
          print("False")
    def insert(self,data):
        nn=box(data)
        self.q.res()
        if self.root==None:
            self.root=nn
            self.q.push(nn)
        else:
            while(True):
                t=self.q.pop()
                if t==-1:
                  print("Error")
                  break
                if t.left==None:
                    t.left=nn
                    if data!=-1:
                      self.q.push(nn)
                    break
                elif t.right==None:
                    t.right=nn
                    if data!=-1:
                      self.q.push(nn)
                    break
    def inorder(self,root):
      if root==None:
        return 1
      else:
        if root.right!=None and root.right.data<root.data:
          return -1
        if root.left!=None and root.left.data>root.data:
          return -1
        t = self.inorder(root.left)
        if t==-1:
          return t
        t = self.inorder(root.right)
        return t
l=ll()
n=int(input())
list1=list(map(int,input().split()))
for i in list1:
    l.insert(i)
l.intrav()