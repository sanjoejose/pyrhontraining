year=int(input())
month=int(input())
if year>=1900 and year<=9999 and month>=1 and month<=12:
  if month in [1,3,5,7,8,10,12]:
    print(31,"Days")
  elif month==2:
    if (year%4==0 and year%100!=0) or year%400==0:
      print(29,"Days")
    else:
      print(28,"Days")
  else:
    print(30,"Days")
else:
  print(0)