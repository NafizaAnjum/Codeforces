t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    if a[0]==a[1] or a[0]==a[2]:
        r=a[0]
    else:
        r=a[1]

    for i in range(n):
        if a[i]!=r:
            print(i+1)
            break