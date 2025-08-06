t=int(input())
for _ in range(t):
    s=input()
    ca=0
    cb=0
    for i in range(5):
        if s[i]=='A':
            ca+=1
        elif s[i]=='B':
            cb+=1
    if max(ca,cb)==ca:
        print("A")
    else:
        print("B")
    