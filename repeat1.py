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
    def dele(self):
       t=self.head
       while t!=None:
          check=t.data
          c=t.next
          ch=t.next.next
          if c.data==check:
             t.next=ch
             c=c.next
             ch=ch.next
             while ch!=None:
                if ch.data==check:
                    c=ch.next
                    ch=ch.next.next
             c=c.next
             ch=ch.next
          t=t.next
         
l=ll()
n=int(input())
while n!=-1:
  l.insert(n)
  n=int(input())
l.dele()
l.trav()