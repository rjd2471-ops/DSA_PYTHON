#Question Remove duplicate in a sorted array in place: Means put unique elements first and for duplicate
#you can can put anything.
nums=[1,1,1,2,3,4,4,7,9,9,10]
i=0
j=i+1
while  j<len(nums):
    while j<len(nums) and nums[i]==nums[j] :
        
        j+=1
    if j<len(nums) :
       nums[i+1]=nums[j]
       i+=1
    
for k in range(i+1, len(nums)):
        nums[k] = "X"
        
print(nums)
#Here time comp is O(N) and space comp is O(1).
#______________________________________________________________________________________________.
#Question Right rotate array by one place.
nums=[5,-2,3,9,0,6,10,7]
nums[:]=[nums[-1]]+nums[0:len(nums)-1]
print(nums)

#_______________________________________________________________________________________________.
#Question Right rotate an array by k place.
nums=[3,9,5,6,7,2]
k=3
n=len(nums)
k=k%n
nums[:]=nums[n-k:n]+nums[0:n-k]

print(nums)
#here space comp is O(N) as python internally create , time comp is O(N).
#Other approch
nums=[3,9,5,6,7,2]
n=len(nums)
k=5
def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
reverse(nums,n-k,n-1)#Reverse last k elements
reverse(nums,0,n-k-1)#Reverse n-k element
reverse(nums,0,n-1)#Reverse all the remaning elelemnt.
print(nums)