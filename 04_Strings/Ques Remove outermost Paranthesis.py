#Ques Remove outermost Paranthesis.


s = "(()())(())"

result = " "

count =0
for ch in s:
    if ch == "(":
        count+=1
        if count>1:
            result+="("
    else:
        count-=1
        if count>0:
            result+=")"
print(result)