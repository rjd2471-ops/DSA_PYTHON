#Ques Valid Anagram .

s = "anagram"

t = "nagaram"

#The simplest way to do this is sort_s == sort_t. Equal then this is valid Angram.

#Let's try the optimal sol for this.


s = "anagram"

t = "nagaram"

d = {}
if len(s)!= len(t):
    print(False)
for i in s:
    d[i] = d.get(i,0)+1

for ch in t:
    if ch not in d:
        print(False)
        break
    
    else:
        if d[ch] == 0:
            print(False)
        else:
            d[ch]-=1
else:
    print(True)

