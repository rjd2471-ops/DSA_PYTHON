#Ques Longest common Prefix.


strs = ["pow","power","powers"]

result = ""
j=-1
for ch in strs[0]:
    j+=1
    for i in range(1,len(strs)):
        if j>= len(strs[i]):
            break
        elif strs[i][j] != ch:
            break
    result+=ch
print(result)