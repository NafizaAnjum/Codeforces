t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    evenc=0
    oddc=0
    for i in range(n):
        if (i%2==0) and (a[i]%2!=0):
            evenc+=1
        elif (i%2!=0) and (a[i]%2==0):
            oddc+=1
    if evenc==oddc:
        print(evenc)
    else:
        print(-1)

        