age=int(input())
year=int(input())
income=int(input())
supply=int(input())
mark=float(input())
atten=float(input())
if year>=2021 and age>=18 and age<21 and supply<=2 and mark>=60 and income<=200000:
    print("Eligible")
elif (supply>2 and mark>=80 and atten>=90 and year>=2021 and age>=18 and age<21 and income<250000):
    print("Partially Eligible")
elif (income>200000 and income<250000 and year>=2021 and age>=18 and age<21 and supply<=2 and mark>=60):
  print("Partially Eligible")
else:
  print("Not Eligible")