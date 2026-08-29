#Bubble sort(Adjacent swap).
nums=[5,1,6,8,2,4,9]
z=len(nums)
for i in range(len(nums)-1):
    left=0
    z-=1
    flage=0
    while left<z:
        right=left+1
        if nums[right]< nums[left]:
            nums[left],nums[right]=nums[right],nums[left]
            flage=1
        left+=1
    if flage==0:
        break
print(nums)
