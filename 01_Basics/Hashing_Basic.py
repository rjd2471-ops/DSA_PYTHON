n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
d={}
for i in n:
    d[i]=d.get(i,0)+1
for j in m:
    if j in d:
        print(d[j])
    else:
        print(0)

#-------------------------------------------------------------------.
#Character hashing .
ass="azyxyyzaaaa"
hash_list=[0]*26
for char in ass:
    ascii_val=ord(char)
    index=ascii_val-97
    hash_list[index]+=1
print(hash_list)
print(ord("a")-32==ord("A"))
#This is most basic concept.