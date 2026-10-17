#Ques Maximum Nesting Depth of the Parentheses.

s = "()(())((()()))"

max_count = count =0

for i in s:
    if i == "(":
        count+=1
    elif i == ")":
        count-=1
    max_count = max(count , max_count)
    
print(max_count)