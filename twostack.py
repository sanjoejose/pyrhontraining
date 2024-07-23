class li:
    def __init__(self,n):
        self.top1=-1
        self.top2=0
        self.stac=[0]*n
    def push1(self,data):
        self.top1+=1
        self.stac[self.top1]=data
    def pop1(self):
      if self.top1==-1:
        print("Stack underflow. pop from stack 1 failed")
        return -1
      t=self.stac[self.top1]
      self.top1-=1
      return t
    def push2(self,data):
        self.top2-=1
        self.stac[self.top2]=data
    def pop2(self):
      if self.top2==0:
        print("Stack underflow. pop from stack 2 failed")
        return -1
      t=self.stac[self.top2]
      self.top2+=1
      return t
    def disp1(self):
      print("Stack 1 Elements:")
      temp=self.top1
      while temp!=-1:
        print(self.stac[temp],'',end="")
        temp-=1
      print()
    def disp2(self):
      temp=self.top2
      print("Stack 2 Elements:")
      while temp!=0:
        print(self.stac[temp],'',end="")
        temp+=1
      print()
n1=int(input())
list1=list(map(int,input().split()))
n2=int(input())
list2=list(map(int,input().split()))
l=li(n2+n1)
for i in range(n1):
  l.push1(list1[i])
for i in range(n2):
  l.push2(list2[i])
l.disp1()
l.disp2()
l1=int(input())
l2=int(input())
for i in range(l1):
  a=l.pop1()
  if a==-1:
    break
for i in range(l2):
  a=l.pop2()
  if a==-1:
    break
l.disp1()
l.disp2()

