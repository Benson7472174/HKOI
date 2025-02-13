n=int(input())
while n!=0:
    b=int(n/1000)
    n=n%1000
    for i in range(b):
        print("1000")
    b=int(n/500)
    n=n%500
    for i in range(b):
        print("500")
    b=int(n/100)
    n=n%100
    for i in range(b):
        print("100")
    b=int(n/50)
    n=n%50
    for i in range(b):
        print("50")
    b=int(n/20)
    n=n%20
    for i in range(b):
        print("20")
    b=int(n/10)
    n=n%10
    for i in range(b):
        print("10")
    break