t=int(input())
s=[]
for _ in range(t):
    n=int(input())
    s.append(n)

f=[]
i=1
while len(f)<1000:
    if i%10!=3 and i%3!=0:
        f.append(i)
    i+=1
for k in s:
    print(f[k-1])