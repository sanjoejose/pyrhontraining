salary=0
sun=int(input())
if sun>8:
  sal=sun*150
  sal=sal
else:
  sal=sun*150
salary=salary+sal
mon=int(input())
if mon>8:
  sal=mon*100
  sal=sal+(mon-8)*15
else:
  sal=mon*100
salary=salary+sal
tue=int(input())
if tue>8:
  sal=tue*100
  sal=sal+(tue-8)*15
else:
  sal=tue*100
salary=salary+sal
wed=int(input())
if wed>8:
  sal=wed*100
  sal=sal+(wed-8)*15
else:
  sal=wed*100
salary=salary+sal
thu=int(input())
if thu>8:
  sal=thu*100
  sal=sal+(thu-8)*15
else:
  sal=thu*100
salary=salary+sal
fri=int(input())
if fri>8:
  sal=fri*100
  sal=sal+(fri-8)*15
else:
  sal=fri*100
salary=salary+sal
sat=int(input())
if sat>8:
  sal=sat*125
  sal=sal
else:
  sal=sat*125
salary=salary+sal
print(salary)