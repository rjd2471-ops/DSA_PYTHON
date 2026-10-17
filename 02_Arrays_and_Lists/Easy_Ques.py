#Question: find the largest element in an array.
nums=[55,32,-97,99,3,67]
def largest(nums):
    larg=float("-inf")
    for i in nums:
        if i> larg:
            larg=i
    return larg
print(largest(nums))
#_____________________________________________________________________________________________.

#Question : find second largest element:
def second_largest(nums):
    first=second=float("-inf")
    temp=None
    if len(nums)<2:
        return
    for i in nums:
        if i>first:
            second=first
            first=i
        elif i>second and i!=first:
            second=i
    return second

print(second_largest(nums))
#_________________________________________________________________________________________.

#Question Check if a list is sorted or not.
def check_sort(nums):
    if len(nums)<=2:
        return True
    a=nums[0]
    b=nums[-1]
    if b>a :
        j=-1
        for i in nums:
            if j!=-1 and nums[j]>i :
                return False
            j+=1
        return True
    else:
        j=-1
        for i in nums:
            if j!= -1 and nums[j]<i:
                return False
            j+=1
        return True
print(check_sort(nums))
#Or improved code for this is.
def check_sort(nums):
    ass=True
    dec=True
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            ass=False
        if nums[i]>nums[i-1]:
            dec=False
            
    return ass or dec
print(check_sort(nums))