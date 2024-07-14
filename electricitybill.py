unit=int(input())
if unit<=200:
  rate=float((0.5*unit))
elif unit<=400:
  rate=float((0.65*unit)+100)
elif unit<=600:
  rate=float((0.80*unit)+200)
else:
  rate=float((1.25*unit)+425)
print("Rs.",int(rate),sep="")