n=int(input())
for i in range (n) :
    s=list(map(int,input().split()))
    s.sort()
    if s[2]==s[0]+s[1]:
        print("YES")
    else:
        print("NO")