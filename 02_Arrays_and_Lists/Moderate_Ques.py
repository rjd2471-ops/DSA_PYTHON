#Question merge two sorted array in a sorted array.
nums1=[1,1,1,2,4,6,7]
nums2=[1,2,3,6,7,8,9,10]
a=len(nums1)
b=len(nums2)

i=0
j=0
result=[]
while i<a or j<b:
    if i==a:
        result.append(nums2[j])
        j+=1

    elif j==b:
        result.append(nums1[i])
        i+=1

    elif nums1[i] <= nums2[j]:
        result.append(nums1[i])
        i+=1

    else:
        result.append(nums2[j])
        j+=1

print(result)
#here the time and space comp is O(N).

#___________________________________________________________________________________________.
#Question Find the missing number in the array.
nums=[9,6,4,2,3,5,7,0,1]
count=0
for i in nums:
    count+=i
n=len(nums)
total=n*(n+1)//2
print(total-count)