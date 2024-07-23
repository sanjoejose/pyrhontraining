class box:
    def __init__(self,data):
        self.data=data
        self.link=None
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
            self.temp.link=nn
            self.temp=nn
    def dis(self):
        t=self.head
        while t.link!=None:
            print(t.data,"->",end="",sep="")
        print(t.data)
t=int(input())
mat=[ll() for _ in range(n*t)]
n,e=map(int,input().split())
qu=[[0,0] for _ in range(e)]
mat=[ll() for _ in range(n)]
for j in range(e):
    st,end=map(int,input().split())
    for k in range(n):
        if st==k:
            mat[k].insert(end)
        if end==k:
            mat[k].insert(st)
for j in range(n):
    mat[j].dis()
            
        
