#Selection sorting.
num=[8,2,6,7,4,2,5,8,1,9]
for i in range(len(num)):
    min_ind=i
    for j in range(i+1,len(num)):
        if num[j]< num[min_ind]:
            min_ind =j
           
    num[i],num[min_ind]=num[min_ind],num[i]    
print(num)
#Here time comp is O(N**2) and space comp is O(1).
#__________________________________________________________________Reverse order.
nums=[8,2,6,7,4,2,5,8,1,9]
for i in range(len(nums)):
    max_ind=i
    for j in range(i+1,len(nums)):
        if nums[j]> nums[max_ind]:
            max_ind=j
    nums[i],nums[max_ind]=nums[max_ind],nums[i]
print(nums)
