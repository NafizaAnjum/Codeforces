t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    cp=[]
    ct=s[0]
    f=False

    for i in range(n):
        if s[i]!=ct:
            cp.append(ct)
            ct=s[i]
        if s[i] in cp:
            print("NO")
            f=True
            break
    if not f:
        print("YES")