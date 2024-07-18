class box:
    def __init__(self,data):
        self.data=data
        self.next=None
class li:
    def __init__(self,n):
        self.head=None
        self.temp=None
    def push(self,data):
        nn=box(data)
        if self.head==None:
            self.head=nn
            self.temp=nn
        else:
            nn.link=self.head
            self.head=nn
    def pop(self):
        if self.head!=None:
            t=self.head.data
            self.head=self.head.next
            return t
        else:
            return -1
st=input()
l=li(len(st))
check=0
for i in range(len(st)):
    if st[i]=='(' or st[i]=='{' or st[i]=='[':
        l.push(st[i])
    elif st[i]==')':
        temp=l.pop()
        if temp!='(':
            print("Not Balanced")
            check=1
            break
    elif st[i]=='}':
        temp=l.pop()
        if temp!='{':
            print("Not Balanced")
            check=1
            break
    elif st[i]==']':
        temp=l.pop()
        if temp!='[':
            print("Not Balanced")
            check=1
            break
if check==0:
    print("Balanced")
