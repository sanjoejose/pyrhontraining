mon=int(input())
rate=int(input())
no=int(input())
if mon in [4,5,6,11,12]:
  rate=float(rate+(rate*20/100))
  print(int(rate*no))
elif mon<11:
  rate=rate
  print(rate*no)
else:
  print("Invalid Input")