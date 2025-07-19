import math

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    d=abs(a-b)
    r=math.ceil(d/10)
    print(r)

