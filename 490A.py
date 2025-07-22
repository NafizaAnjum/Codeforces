n=int(input())
a=list(map(int,input().split()))
p=[]
m=[]
s=[]
for i in range(n):
    if a[i]==1:
        p.append(i+1)
    elif a[i]==2:
        m.append(i+1)
    elif a[i]==3:
        s.append(i+1)
team=min(len(p),len(s),len(m))
print(team)
for i in range(team):
    print(p[i],m[i],s[i])