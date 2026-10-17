#Question Sum of 4 numbers.
#In simple words arr[i]+arr[j]+arr[k]+arr[l]==target such that i!=j!=k!=l.
nums=[1,0,-1,0,-2,2]
result=[]
nums.sort()
target=0
for i in range(len(nums)-3):
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,len(nums)-2):
        if j>i+1 and nums[j]==nums[j-1]:
           continue
        left=j+1
        right=len(nums)-1
        while left<right:
            total=nums[i]+nums[j]+nums[left]+nums[right]
            if total==target:
                result.append((nums[i],nums[j],nums[left],nums[right]))
                
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right-=1
            elif total < target:
                 left += 1
            else:
                right-=1
print(result)
#Time comp is O(n log n) + O(n³) and space comp is Space Complexity = O(n³) in wrost case othewise O(K).
                
    