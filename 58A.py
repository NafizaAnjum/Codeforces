s=input()
S="hello"
j=0
for i in s:
    if i==S[j]:
        j+=1
    if j==len(S):
        break
if j==len(S):
    print("YES")
else:
    print("NO")