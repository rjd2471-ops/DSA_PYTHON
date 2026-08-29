#Insertion sorting.
nums=[3,5,6,4,8,9,10,7,1]
for i in range(1,len(nums)):
    key=nums[i]
    j=i-1
    
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key    
        
       
print(nums)
#Here tie comp is O(N**2) and space comp is O(1).
        
    