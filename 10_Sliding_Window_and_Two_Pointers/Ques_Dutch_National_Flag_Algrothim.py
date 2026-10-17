#Leet_code question 75.

def partion(arr,low,high):
        pivot = arr[low]

        i = low
        j = high
        while i<j:
            while arr[i] <= pivot and i< high:
                i+=1
            while arr[j]> pivot and j>= low:
                j-=1
            if i<j:
             arr[i],arr[j] = arr[j], arr[i]
        arr[j],arr[low] = arr[low],arr[j]
        return j

def quick(num,low,high):
            
    if low>= high:
        return
    p = partion(num,low,high)
    quick(num,low,p-1)
    quick(num,p+1,high)

##############################################################
    
#Other sol for this question is.
count = [0,0,0]

for i in nums:
    count[i]+=1
i = 0
for j in range(3):
    while count[j] >0:
        nums[i] = j
        count[j]-=1
        i+=1
        
#Let's try the other sol for this is which is Dutch National Flag.
        
        
class Solution(object):
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                # Put 0 in the 0-region
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # 1 is already in the middle region
                mid += 1

            else:  # nums[mid] == 2
                # Put 2 in the 2-region
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1