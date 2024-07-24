class box:
  def __init__(self,d):
    self.data = d
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
        else:
            self.temp.next=nn
            self.temp=nn
    def trav(self):
        t=self.head
        while t!=None:
            print(t.data,"",end="")
            t=t.next
        print()
    def p(self):
       p1=self.head
       p2=self.head
       while p2!=None and p2.next!=None:
          p1=p1.next
          p2=p2.next.next
       
       print(p1.data)
       
l=ll()
n=int(input())
while n!=-1:
  l.insert(n)
  n=int(input())
l.trav()
l.p()
