#Question Move all the Zeros in a list into last without destrubing the order.
nums=[1,0,2,4,3,0,0,3,5,1]
i=0
j=i+1
while j< len(nums):
    while j<len(nums) and nums[j]==0:
        j+=1
    while i<len(nums) and nums[i]!=0:
        i+=1
    if j<len(nums) and i<len(nums):
        nums[i]=nums[j]
        nums[j]=0
        i+=1
        j+=1
    

print(nums)
#Here time comp is O(N) and space comp is O(1).
#Cleaner code
nums=[1,0,2,4,3,0,0,3,5,1]
i=0
for j in range(len(nums)):
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
print(nums)


#____________________________________________________________________________________________________.
#question maximum Consecutive ones in the list is.
nums=[1,1,0,1,0,1,1,1,1,0,1,1]
count=0
max_count=0
for i in nums:
    if i==1:
        count+=1
        max_count=max(count,max_count)  
    else :
        count=0
print(max_count)

#______________________________________________________________________________________________.
#Question sum of two num is equal to target find their index.
nums=[5,9,1,2,4,15,6,3]
target=13
d={}

for i in range(len(nums)):
    remaning=target-nums[i]
    if remaning in d:
        print([d[remaning],i])
        break
    d[nums[i]]=i
#Here time comp and space comp is O(N).



#_____________________________________________________________________________________________.
#Question Find the maximum sum of the subarray.
def subarray(nums):#this code may note work for some cases it only works for +ive nums mostely.
    total=nums[0]
    max_total=nums[0]
    for i in range(1,len(nums)):
        
        if total<0:
            total=0
        if nums[i]<0 :
            if total> abs(nums[i]) :
                total+=nums[i]
            else:
                max_total=max(max_total,total)
                total=0
        else:
            total+= nums[i]
        max_total=max(total,max_total)
    return max_total
print(subarray([-2,1,-3,4,-1,2,1,-5,4,9,-1]))
#Other approch for this is. This is much cleaner approch for this is.
def subarray(nums):
    total=nums[0]
    max_total=nums[0]
    for i in range(1,len(nums)):
        total=max(nums[i],total+nums[i])
        max_total=max(total,max_total)
    return max_total
print(subarray([-2,1,-3,4,-1,2,1,-5,4]))
            


#_________________________________________________________________________________________________.
#Question Stock buy and sell to get maximum profit.
#Simple means the difference bw buy and sell is maximum.
price=[7,2,1,5,6,4,8]
min_price=float("inf")
max_profit=0
for i in range(len(price)):
    min_price=min(min_price,price[i])
    profit=price[i]-min_price
    max_profit=max(max_profit,profit)
print(max_profit)

#___________________________________________________________________________________________________.
#Question Rearrange the num according to sign without changing their order.
#Simple meaning +ive, -ive and so on without changing their oreder as positive and negative.
nums=[5,-3,-1]
n=len(nums)
i=1
j=1
result=[nums[0]]
while (i<n and result[-1]<0) or (j<n and result[-1]>0):
    if result[-1]<0:
     while i<n and nums[i]<0:
        i+=1
     if i< n :
        result.append(nums[i])
        i+=1
    else:
     while j<n and nums[j]>0 :
        j+=1
     if j<n :
        result.append(nums[j])
        j+=1
    
print(result)




#____________________________________________________________________________________________.
#Question Find the longest consective seq in an array.
nums=[1,99,101,98,2,5,3,100,1,1]
a=set(nums)
b=sorted(list(a))
count=1
max_count=0
for i in range(len(b)-1):
    if b[i]+1==b[i+1] :
        count+=1
        max_count=max(max_count,count)
    else:
        count=1
print(max_count)
#Here time comp is o(NlogN) and space comp is O(N).

#Here the most optimal sol is.
nums=[1,99,101,98,2,5,3,100,1,1]
a=set(nums)
max_count=0
for num in a:
    if num-1 not in a:
        curr=num
        count=1
        while curr+1 in a:
            count+=1
            curr+=1
        max_count=max(max_count,count)
print(max_count)
#here the time comp is O(N) and space comp is also O(N).



    
