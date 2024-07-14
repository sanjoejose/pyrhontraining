num=int(input())
if num>99 and num<1000:
  num=int(num/10)
  num=num%10
  if num%3==0:
    print("Trendy Number")
  else:
    print("Not a Trendy Number")
else:
  print("Invalid Number")