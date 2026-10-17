#Count the number of digits in a number.
#So, here we see in the previous case that time comp is O(log(N)) or O(No of digits)
#These are almot equal so we can use int(log(N)+1).
from math import *
def count_digit(n):
    if n==0:
        return 1
    return int(log10(n)+1)
print(count_digit(123456))
#----------------------------------------------------------------------------
import math
def count_digit(n):
    if n==0:
        return 1
    return int(math.log10(n)+1)
print(count_digit(123456))