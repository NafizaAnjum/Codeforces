a,b=map(int,input().split())
if a>=b:
    r=(a-b)//2
    print(b,r)
elif b>=a:
    r=(b-a)//2
    print(a,r)
