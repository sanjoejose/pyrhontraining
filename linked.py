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
            print(t.data)
            t=t.next
    def dele(self,key):
        if self.head.data==key:
           self.head=self.head.next
        else:
            t=self.head
            while t.next.data!=key:
                t=t.next
            t.next=t.next.next
l=ll()
n=int(input())
while n!=-1:
  l.insert(n)
  n=int(input())
print("Enter value to delete :")
n=int(input())
l.dele(n)
l.trav()