t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    s=max(min(max(2*a,b),max(a,2*b)),max(a,b))
    print(s*s)