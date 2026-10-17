#Ques Sort character by fequency.


s = "tree"

d = {}
for ch in s:
    d[ch] = d.get(ch,0)+1
result = ""
sort_d = sorted( d.items(),key = lambda x: x[1], reverse = True )

for char , freq  in sort_d:
    result+= char*freq
    
print(result)