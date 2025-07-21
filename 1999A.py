t=int(input())

r=0
for _ in range(t):
    n=int(input())
    sum=0
    for _ in range(2):
        r=n%10
        sum+=r
        n=n/10
    print (int(sum))
