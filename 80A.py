def prime(x):
    if x<2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

n,m=map(int,input().split())

np=n+1
while not prime(np):
    np+=1 

if np==m:
    print("YES")
else:
    print("NO")