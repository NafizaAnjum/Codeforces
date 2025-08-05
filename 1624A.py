t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    mx=max(s)
    mn=min(s)
    print(mx-mn)