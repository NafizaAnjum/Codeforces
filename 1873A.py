t=int(input())
for _ in range(t):
    s=input()
    if s in ("abc", "acb", "bac", "cba"):
        print("YES")
    else:
        print("NO")