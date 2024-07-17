class box:
    def __init__(self,data,h):
        self.data=data
        self.next=h
class ll:
    def __init__(self):
        self.head=None
        self.temp=None
    def insert(self,data):
        if self.head==None:
            nn=box(data,None)
            self.head=nn
            self.head.next=self.head
            self.temp=nn
        else:
            nn=box(data,self.head)
            self.temp.next=nn
            self.temp=nn
            self.temp.next=self.head
    def trav(self):
        t=self.head
        while t.next!=self.head:
            print(t.data)
            t=t.next
        print(t.data)
l=ll()
n=int(input())
while n>-1:
    l.insert(n)
    n=int(input())
l.trav()