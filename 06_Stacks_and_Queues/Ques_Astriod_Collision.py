#Ques Astroid Collision.

nums=[4,7,1,1,2,-3,-7,17,15,-18,-19]

stack=[]

for i in nums:
    alive= True
    
    while stack and stack[-1]>0 and i<0:#collision happens.
        if abs(i) >stack[-1]:
            stack.pop()
            continue
        
        elif stack[-1] == abs(i):
            stack.pop()
            alive=False#alive False means that does not append that value into the stack.
            break
        
        else:
            alive= False
            break
    
    if alive:
        stack.append(i)
        
print(stack)
        