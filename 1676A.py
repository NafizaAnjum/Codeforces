t=int(input())

for _ in range(t):
    a=input()
    ls=0
    rs=0
    for i in range(3):
        ls+=int(a[i])
    for i in range(3,6):
        rs+=int(a[i])
    if(ls==rs):
        print("YES")
    else:
        print("NO")
