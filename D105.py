from datetime import datetime
y1,m1,d1=map(int,input().split())
y2,m2,d2=map(int,input().split())
date1=datetime(y1,m1,d1)
date2=datetime(y2,m2,d2)
if date1 < date2:
    print("Before")
elif date1 > date2:
    print("After")
else:
    print("Same")