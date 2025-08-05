t=int(input())
for _ in range(t):
    h,m=map(int,input().split())
    t=(60*h)+m
    print(1440-t)