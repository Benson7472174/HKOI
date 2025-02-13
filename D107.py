n=int(input())
s_num=n**0.5
s_int=int(s_num)
t_num=(-1+((1+8*n)**0.5))/2
t_int=int(t_num)
if s_num==s_int:
    s=1
else:
    s=0
if t_num==t_int:
    t=1
else:
    t=0
if s==t==1:
    print("Both")
elif s==1:
    print("Square")
elif t==1:
    print("Triangular")
else:
    print("Neither")