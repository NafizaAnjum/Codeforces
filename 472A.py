def c(x):
    if x<=3:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return True
    return False
n=int(input())
for a in range(4,n):
    b=n-a
    if c(a) and c(b):
        print(a,b)
        break
    