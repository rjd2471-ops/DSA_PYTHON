#Check pallandrom.
def check_pall(n):
    d=len(str(n))
    k=d-1
    for j in range(d):
        if (str(n))[j]!= (str(n))[k]:
            return False
        k-=1
    return True
print(check_pall(112211))#Here time comp is O(D*D)
#-------------------------------------------------------------------
def check_pall(n):
    s = str(n)
    d = len(s)
    k = d - 1

    for j in range(d):
        if s[j] != s[k]:
            return False
        k -= 1

    return True
print(check_pall(112211))
#Here time comp is O(D).
#-------------------------------------------------------------
def check_pall(n):
    s = str(n)
    return s == s[::-1]
print(check_pall(112211))#Here also time and space comp is O(D).