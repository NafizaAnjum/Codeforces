n = int(input())
a = list(map(int, input().split()))

c = 0
max= a[0]
min= a[0]

for i in range(1, n):
    if a[i] > max:
        max= a[i]
        c += 1
    elif a[i] < min:
        min= a[i]
        c += 1

print(c)
