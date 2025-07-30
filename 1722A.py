t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    s1="Timur"
    if len(s)==len(s1) and sorted(s)==sorted(s1):
        print("YES")
    else:
        print("NO")