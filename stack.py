class li:
    def __init__(self,n):
        self.top=-1
        self.stac=[0]*n
    def push(self,data):
        self.top+=1
        self.stac[self.top]=data
    def pop(self):
        t=self.stac[self.top]
        self.top-=1
        return t
st=input()
l=li(len(st))
check=0
for i in range(len(st)):
    if st[i]=='(' or st[i]=='{' or st[i]=='[':
        l.push(st[i])
    elif st[i]==')':
        temp=l.pop()
        if temp!='(':
            print("No")
            check=1
            break
    elif st[i]=='}':
        temp=l.pop()
        if temp!='{':
            print("No")
            check=1
            break
    elif st[i]==']':
        temp=l.pop()
        if temp!='[':
            print("No")
            check=1
            break
if check==0:
    print("Yes")
