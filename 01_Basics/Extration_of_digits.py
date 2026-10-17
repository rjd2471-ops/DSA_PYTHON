#Extraction of digits from a number.
num=56789
while num!=0:
    print(num%10)
    num=num//10
#This code for reverse order
def fun(n):
    if n==0:
        return 
    fun(n//10)
    print(n%10)
(fun(56789))
#Here the time comp is O(log(N)) or O(No of digits).