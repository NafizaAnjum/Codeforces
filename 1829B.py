t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    maxc=0
    for i in range(n):
        if a[i]==0 :
            c+=1
            maxc=max(c,maxc)
        else:
            c=0
    print(maxc)
