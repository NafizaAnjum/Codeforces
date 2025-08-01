t=int(input())
for _ in range(t):
    n=input().strip()
    d=int(n[0])
    l=len(n)
    print(((d-1)*10)+(l*(l+1))//2)
