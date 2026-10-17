#Ques Maximum Points You Can Obtain from Cards | But here is condition that you can pick card from first or last

nums=[1,2,3,4,5,6,1]

k=3 #That means you can pick three cards.

left_sum=0
right_sum=0



for i in range(k):#This is the sum of first K cads from the left side or beganing.
    left_sum+=nums[i]

max_sum= left_sum
i=1   
for j in range(len(nums)-1, len(nums)-1-k,-1):
    left_sum-= nums[k-i]
    i+=1
    right_sum+= nums[j]
    
    max_sum= max(max_sum, left_sum+right_sum)
    
print(max_sum)
#Here the time comp is O(K) and space comp is O(1).