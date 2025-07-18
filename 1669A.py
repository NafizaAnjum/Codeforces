n=int(input())
for i in range(n):
    r=int(input())
    if r>=1900:
        X=1
    elif 1600<=r and r<=1899:
        X=2
    elif 1400<=r and r<=1599:
        X=3
    elif r<=1399:
        X=4
    print(f"Division {X}")
    
        