t=int(input())
for _ in range(t):
    b=input()
    a=b[0]
    n=len(b)
    for i in range(1,n,2):
        a+=b[i]
    print(a)
