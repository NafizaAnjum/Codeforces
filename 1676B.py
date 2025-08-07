t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    m=min(s)
    c=0
    for i in range(n):
        if s[i]==m:
            i+=1
        elif s[i]!=m:
            c+=s[i]-m
    print(c)
            