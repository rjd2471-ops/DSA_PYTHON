#Question sum of 3 number equal to 0.
# arr[i]+arr[j]+arr[k]=0 such that i!=j!=k.
arr =[-100,-70,-60,110,120,130,160]
result=[]
arr.sort()
for i in range(len(arr)-2):
    if i>0 and arr[i]==arr[i-1]:
        continue
    left=i+1
    right=len(arr)-1
    
    while left<right:
        total=arr[i]+arr[left]+arr[right]
        
        if total==0:
            result.append((arr[i],arr[left],arr[right]))
            left+=1
            right-=1
            
            while left<right and arr[left]==arr[left-1]:
                left+=1

            while left<right and arr[right]==arr[right+1]:
                right-=1
        elif total<0:
            left+=1
        else:
            right-=1
print(result)
#Here time comp is O(N**2) and space comp is Space Complexity:
                         #- O(k) including result storage and in wrost case it will become O(N**2).
        
    
      
    


