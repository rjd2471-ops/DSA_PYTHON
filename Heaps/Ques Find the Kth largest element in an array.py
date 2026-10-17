#Ques Find the Kth largest element in an array.

import heapq
nums = []
arr = [3,2,3,1,2,4,5,5,6,1]

k = 4

n = len(arr)

for i in range(k):
    heapq.heappush(nums,arr[i])
    
for j in range(k,n):
    if arr[j]> nums[0]:
        heapq.heappop(nums)
        heapq.heappush(nums,arr[j])
print(nums[0])

#Here time comp is O(KlogK+(N-K)logK)~= NlogK, and space comp is O(K).


#Let's try the most optimal sol for this using.
#Quick select and partition Algrithim.


# Find Kth Largest using Quick Select

arr = [3,2,3,1,2,4,5,5,6,1]

k = 4

def partion(arr,low,high):
    pivot = arr[low]
    
    i = low
    j = high
    
    while i<j:
        while arr[i] <= pivot and i <= high-1 :
            i+=1
        while arr[j] > pivot and j >= low+1 :
            j-=1
        if i<j:
           arr[i],arr[j] = arr[j],arr[i]
    arr[j],arr[low] = arr[low],arr[j]
    return j
def quick(num,low,high,k):
    if low<= high:
        a = partion(num,low,high)
        
        if a == k:
            return num[k]
        elif a >k:
           return quick(num,low,a-1,k)
        else:
            return quick(num,a+1,high,k)
target = len(arr) - k    
print(quick(arr,0,len(arr)-1,target))
        

#Here time comp is O(N).
