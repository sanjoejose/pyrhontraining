class box:
  def __init__(self,d):
    self.data = d
    self.link=None
class ll:
  def __init__(self):
    self.head=None
    self.temp=None
  def beg(self,data):
    nn=box(data)
    if self.head==None:
      self.head=nn
      self.temp=nn
    else:
      nn.link=self.head
      self.head=nn
  def end(self,data):
    nn=box(data)
    if self.head==None:
      self.head=nn
      self.temp=nn
    else:
      self.temp.link=nn
      self.temp=nn
  def trav(self,h):
    t=self.head
    while t!=None:
      print(t.data)
      t=t.link
l=ll()
n=int(input())
while n!=-1:
  l.beg(n)
  n=int(input())
l.trav(n)