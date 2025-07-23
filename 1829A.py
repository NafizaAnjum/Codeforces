n=int(input())
s1="codeforces"
for _ in range(n):
    s2=input()
    j=0
    c=0
    for i in s2:
        if i!=s1[j]:
            c+=1
        j+=1
    print(c)