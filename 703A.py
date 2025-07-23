n=int(input())
M=0
C=0
d=0
for _ in range(n):
    m,c=map(int,input().split())
    if m==c:
        d+=1
    elif m>c:
        M+=1
    elif c>m:
        C+=1
if(d==n) or (M==C):
    print("Friendship is magic!^^")
elif M>C:
    print("Mishka")
elif C>M:
    print("Chris")