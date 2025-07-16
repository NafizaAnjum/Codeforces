n=int(input())
arr=map(int,input().split())
p=0
c=0
for a in arr:
    if(a==-1):
        if(p>0):
            p-=1
        else:
            c+=1
    else:
        p+=a
    
print(c)
   