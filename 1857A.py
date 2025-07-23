t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    s = sum(a)
    
    if s % 2 == 1:
        print("NO")
    else:
        print("YES")


  