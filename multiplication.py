n=int(input("Enter n\n"))
m=int(input("Enter m\n"))
i=1
print("The multiplication table of",n,"is")
while i<=m:
  print(i,"*",n,"=",(i*n),sep="")
  i=i+1