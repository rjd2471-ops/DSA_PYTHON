#Check Armstrong ie 153=1**3+5**3+3**3
def check_armstrong(n):
    l=len(str(n))
    s=n
    total=0
    while s!=0 and total<=n:
        d = s % 10
        total += d**l
        s=s//10
    return total == n
    
print(check_armstrong(153))