cost=list(map(int,input().split()))
s=input().strip()
calorie=0
for char in s:
    a=int(char)
    calorie+=cost[a-1]
print(calorie)