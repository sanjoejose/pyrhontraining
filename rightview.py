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
    def push2(self,data):
       if self.rear==-1:
          self.rear+=1
          self.front+=1
          self.que[self.rear]=data
       elif data not in self.que:
          self.rear+=1
          self.que[self.rear]=data
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
        self.q2=qu()
        self.temp=None
    def intrav(self):
        self.inorder(self.root)
    def insert(self,data):
        nn=box(data)
        self.q.res()
        if self.root==None:
            self.root=nn
            self.q.push(nn)
            self.temp=nn
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
                      self.temp=nn
                    break
                elif t.right==None:
                    t.right=nn
                    if data!=-1:
                      self.q.push(nn)
                      self.temp=nn
                    break
    def inorder(self,root):
        if root==None:
            return
        else:
            if root.data!=-1:
            	self.q2.push2(root)
            if root.right==None or root.right.data==-1:
              self.inorder(root.left)
            self.inorder(root.right)
            if root==self.root:
              self.q2.push2(self.temp)
l=ll()
list1=input().split()
i=0
while i<len(list1):
  if list1[i]=='N':
    l.insert(-1)
  else:
    l.insert(int(list1[i]))
  i+=1
l.intrav()