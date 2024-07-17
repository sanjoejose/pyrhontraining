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
    def swap(self):
       t1=self.head
       t2=t1.next
       while t2!=None:
          print(t2.data)
          print(t1.data)
          t1=t2.next
          if t1==None:
            return
          t2=t1.next
       print(t1.data)
l=ll()
n=int(input())
count=0
while n>-1:
  l.insert(n)
  n=int(input())
  count+=1
if count==0:
  print("List is empty")
else:
  l.swap()