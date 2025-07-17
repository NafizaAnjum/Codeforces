n,k,l,c,d,p,nl,np=map(int,input().split())
toast=(k*l)/nl
lime=c*d
salt=p/np

r=min(toast,lime,salt)/n
print(int(r))