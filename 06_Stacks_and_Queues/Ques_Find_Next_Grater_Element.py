#Ques Find the Next Grater Element.

nums=[19,4,2,11,6,5,3,10]
ans=[]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        
        if nums[j]> nums[i]:
            ans.append(nums[j])
            break
    else:
       ans.append(-1)
    
print(ans)
#This is the Brute force approch for this and here time comp is O(N**2) and space comp is O(N).

#Let's try the optimal sol.
nums=[19,4,2,11,6,5,3,10]
ans=[-1]*(len(nums))

stack=[]

for i in range(len(nums)-1,-1,-1):
    
    while stack and stack[-1]<= nums[i]:
        stack.pop()
        
    if stack:
        ans[i]= stack[-1]
        
    stack.append(nums[i])
    
print(ans)
