t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if b==c:
        print (a)
    elif a==c:
        print(b)
    else:
        print(c)