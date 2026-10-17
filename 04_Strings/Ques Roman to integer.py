#Ques Roman to integer.

d = {"I":"1" , "V":"5", "X":"10", "L":"50" , "C":"100" , "D":"500" , "M":"1000"}

s = "MCMXCIV"

n = len(s)
num = 0
i=0
while i <n:
    if i!= n-1:
        
        if int(d[s[i]]) >= int(d[s[i+1]]):
            num += int(d[s[i]])
            
        else:
            num += int(int(d[s[i+1]])- int(d[s[i]]))
            i+=1
    else:
        num += int(d[s[i]])
        
    i += 1
print(num)
            
            