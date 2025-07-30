t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    
    n_slv=set()
    c=0
    for i in s:
        c+=1
        if i not in n_slv:
            c+=1
            n_slv.add(i)
    print(c)
