class box:
    def __init__(self,data,p):
        self.data=data
        self.next=None
        self.prev=p
class ll:
    def __init__(self):
        self.head=None
        self.temp=None
    def insert(self,data):
        if self.head==None:
            nn=box(data,None)
            self.head=nn
            self.temp=nn
        else:
            nn=box(data,self.temp)
            self.temp.next=nn
            self.temp=nn
    def nthnode(self,n):
        t=self.temp
        for i in range(n):
            if t==None:
                print("Invalid")
                return
            t=t.next
        print(t.data)
l=ll()
n=int(input())
while n>-1:
    l.insert(n)
    n=int(input())
n=int(input())
l.nthnode(n)
            