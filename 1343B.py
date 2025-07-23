t= int(input())

for _ in range(t):
    n=int(input())
    if (n//2)%2==1:
        print("NO")
    else:
        print("YES")
        e=[]
        o=[]
        for i in range(2,n+1,2):
            e.append(i)
        for i in range(1,n-1,2):
            o.append(i)
        ol=sum(e)-sum(o)
        o.append(ol)
        print(*e+o)
    

