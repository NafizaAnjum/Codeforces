t=int(input())
for _ in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    c1=0
    c2=0
    for i in range(n):
        if c[i]==1:
            c1+=1
        elif c[i]==2:
            c2+=1
    
    if c1%2==0 and c2%2==0:
        print("YES")
    elif c2%2!=0 and c1%2==0 and c1>0:
        print("YES")
    else:
        print("NO")

