import math
a=int(input(""))
b=int(input(""))
c=int(input(""))
c=math.radians(c)
d=a*b
d=d/2
d=d*math.sin(c)
print("%.3f"%d)