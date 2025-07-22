n,k=map(int,input().split())
a=map(int,input().split())
c=0
for y in a:
    if 5-y>=k:
        c+=1
print(int(c/3))