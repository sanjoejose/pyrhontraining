import math
x2=int(input())
y2=int(input())
x1=3
y1=4
x=float(x2-x1)
x=x*x
res=math.floor(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
print(res)