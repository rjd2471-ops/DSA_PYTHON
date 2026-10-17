#Prime factorising of a number.
def factor(n):
    fact=[]
    r=2
    while n!=1 and r<=n:
        if n%r==0 :
            fact.append(r)
            n=n//r
        else:
            r+=1
    return fact
print(factor(153))
#Here time comp is O(N).
#----------------------------------------------------------------------------------
def factor(n):
    fact=[]
    r=2
    while r*r<=n :
        if n%r==0 :
            fact.append(r)
            n=n//r
        else:
            r+=1
    if n>1:
        fact.append(n)
        
    return fact
print(factor(153))
#Here time comp is O(N**.5)
