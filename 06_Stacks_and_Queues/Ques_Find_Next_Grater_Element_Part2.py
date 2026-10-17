#Ques Find the  next Gratest Element part two.

nums=[2,10,12,1,11]

ans=[-1]* len(nums)

stack=[]
for i in range(len(nums)-1,-1,-1):
    
    while stack and stack[-1]<= nums[i]:
        stack.pop()
        
    stack.append(nums[i])


for i in range(len(nums)-1,-1,-1):
    
    while stack and stack[-1]<= nums[i]:
        stack.pop()
        
    if stack:
       ans[i]= stack[-1]
    stack.append(nums[i])
    
print(ans)


#This is also its solution.


nums=[2,10,12,1,11]

ans=[-1]* len(nums)

stack=[]
n=len(nums)
for i in range(2*len(nums)-1,-1,-1):
    
    while stack and stack[-1]<= nums[i%n]:
        stack.pop()
    
    if i<len(nums):
        if stack:
            ans[i]=stack[-1]
        
    stack.append(nums[i%n])
    
print(ans)

