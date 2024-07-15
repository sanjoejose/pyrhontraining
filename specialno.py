n1=int(input())
n2=int(input())
num=n1
while num<=n2:
  temp=num
  x=num%10
  num=int(num/10)
  y=num%10
  if (x+y)+(x*y)==temp:
    print(temp)
  num=temp+1