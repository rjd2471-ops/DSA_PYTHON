#Ques largest odd number in a string.

nums = "6783842"
maxi = 0
for i in nums:
    if int(i)%2==1:
        maxi = max(maxi,int(i))
print(maxi)