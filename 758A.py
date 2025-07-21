n=int(input())
a=list(map(int, input().split()))
m=max(a)
s=0
for i in a:
    d=m-i
    s+=d
print(s)