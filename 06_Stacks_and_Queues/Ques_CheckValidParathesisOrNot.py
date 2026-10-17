#Ques is this is a valid Parathesis.

s="[{()}]"
pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}
stack=[]
for i in s:
    
    if i in "[({" :
        stack.append(i)
    else:
        e= stack.pop()
        
        if e==pairs[i]:#Pairs[i] is the the val and i is the key.
            continue
        else:
            print(False)
            break

else:
    print(len(stack)==0)