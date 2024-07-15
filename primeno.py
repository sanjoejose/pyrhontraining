n=int(input())
count=0
num=2
while num<=n:
  check=0
  for i in range(2,int(num/2+1)):
    if num%i==0:
      check=check+1
      break
  if check==0:
    count=count+1
    print(num,end=" ")
  num=num+1