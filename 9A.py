from math import gcd
y,w=map(int,input().split())
m=max(y,w)
a=6-(m-1)

g=gcd(a,6)
n=a//g
d=6//g
print(f"{n}/{d}")
