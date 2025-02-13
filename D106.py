n=int(input())
l=int(n%100)
if l in(11,12,13):
    print(str(n)+"th")
else:
    k=n%10
    if k==1:
        print(str(n)+"st")
    elif k==2:
        print(str(n)+"nd")
    elif k==3:
        print(str(n)+"rd")
    else:
        print(str(n)+"th")
