t=int(input())
for _ in range(t):
    num=list(map(int,input().split()))
    winner=sorted(num)[2:]

    winner1=max(num[0],num[1])
    winner2=max(num[2],num[3])

    if set(winner)=={winner1,winner2}:
        print("YES")
    else:
        print("NO")