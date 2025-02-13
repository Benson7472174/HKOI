import math
a,b,c=map(int,input().split())
d=(b*b)-(4*a*c)
if d<0:
    print("None")
elif d==0:
    answer=-b/(2*a)
    print("%.3f"%answer)
elif d>0:
    e=math.sqrt(d)
    ao=(-b-math.sqrt(d))/(2*a)
    at=(-b+math.sqrt(d))/(2*a)
    print("%.3f"%ao)
    print("%.3f"%at)