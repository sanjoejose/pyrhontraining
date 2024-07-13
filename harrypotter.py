a=input()
if (a[0]=="-")or(a[0]=="+"):
    l=int(a[1])
    f=int(a[4])
else:
    l=int(a[0])
    f=int(a[3])
sum=f+l
print(sum)