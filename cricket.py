ball=int(input())
total=int(input())
curr=int(input())
curb=int(input())
over=int(ball/6)
rem=float(int(curb/6)+float((curb%6)/10))
crunr=float(curr/rem)
rr=float(total/over)
print(over)
print(rem)
print(round(crunr,1))
print(round(rr,1))
if(crunr>=rr):
  print("Eligible to Win")
else:
  print("Not Eligible to Win")