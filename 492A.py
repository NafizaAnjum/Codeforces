n=int(input())
c=0
i=0
while(True):
    i+=1
    c+=(i*(i+1))//2
    if c>n:
        print(i-1)
        break
    