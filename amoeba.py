n=int(input())
count=2
fib0=0
fib1=1
while count<n:
    temp=fib0+fib1
    fib0=fib1
    fib1=temp
    count=count+1
print(fib1)