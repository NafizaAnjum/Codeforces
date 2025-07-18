n=int(input())
c=list(map(int,input().split()))

s=0
d=0
t=0
l=0
r=n-1

while(l<=r):
    if c[l]>c[r]:
        rs=c[l]
        l+=1
    else:
        rs=c[r]
        r-=1
    if t%2==0:
        s+=rs
    else:
        d+=rs
    t+=1

print(s,d)
