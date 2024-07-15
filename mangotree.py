row=int(input())
col=int(input())
n=int(input())
n=n-1
x=int(n/col)
y=n%col
if x==0 or y==0 or (y==col-1):
  print("Yes")
else:
  print("No")
