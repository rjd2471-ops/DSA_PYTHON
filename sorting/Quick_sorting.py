#Quick sort.
#So for this we have need to pick a pivot and then put that into the correct position.
nums=[4,1,7,6,3,2,8]
def partion(nums,low,high):
    i=low
    j=high
    
    pivot=nums[low]
    while j>i:
        while nums[i]<= pivot and i<=high-1:
            i+=1
        while nums[j]> pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j
def quick_sort(nums,low,high):
    if low<high:
        p_ind=partion(nums,low,len(nums)-1)
        quick_sort(nums,low,p_ind-1)
        quick_sort(nums,p_ind+1,high)
    
    return nums
        
print(quick_sort(nums,0,len(nums)-1))
#Time comp in best and avg case is O(N*LogN) and space comp is O(LOgN)(Stack space).
#In wrost case its time comp is O(N*N), if all num are same in that case.
