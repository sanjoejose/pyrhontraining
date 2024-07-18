class box:
  def __init__(self,data):
    self.data=data
    self.next=None
class ll:
  def __init__(self):
    self.head=None
    self.temp=None
  def insert(self,data):
        nn=box(data)
        if self.head==None:
            self.head=nn
            self.temp=nn
        elif self.head.data>=data:
            nn.next=self.head
            self.head=nn
        elif self.temp.data<=data:
           self.temp.next=nn
           self.temp=nn
        else:
            t=self.head
            while t.next!=None:
                if t.next.data>=data:
                    break
                t=t.next
            nn.next=t.next
            t.next=nn
  def trav(self):
    t=self.head
    while(t.next!=None):
      print(t.data,"->",sep="",end="")
      t=t.next
    print("NULL")
  def create(self,lin1,lin2):
    p1=lin1.head
    p2=lin2.head
    while p1!=None and p2!=None:
      if p1.data<p2.data:
        self.insert(p1.data)
        p1=p1.next
      else:
        self.insert(p2.data)
        p2=p2.next
    while p1!=None:
      self.insert(p1.data)
      p1=p1.next
    while p2!=None:
      self.insert(p2.data)
      p2=p2.next
l1=ll()
l2=ll()
l3=ll()
n=int(input())
list1=list(map(int,input().split()))
for i in range(n):
  l1.insert(list1[i])
n=int(input())
list2=list(map(int,input().split()))
for i in range(n):
  l2.insert(list2[i])
l3.create(l1,l2)
l3.trav()