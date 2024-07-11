import math
tot=int(input())
lon=int(input())
black=int(input())
lons=math.floor(tot*lon/100)
tot=tot-lons
blacks=math.floor(tot*black/100)
tot=tot-blacks
rem=int(tot/3)
print(lons)
print(blacks)
print(rem)
