t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mi=a.index(min(a))
    a[mi]+=1
    ans=1
    for i in a:
        ans*=i
    print(ans)
        
        