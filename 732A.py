k,r =map(int,input().split())
c=1
while True:
    n=k*c
    if n%10==r or n%10==0:
        print(c)
        break;
    c+=1