s=list(map(int,input().split()))
m=max(s)
for i in s:
    r=m-i
    if r!=0:
        print(r,end=" ")
    