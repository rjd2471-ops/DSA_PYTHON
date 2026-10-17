#Merge Sorting(Divide and merge).


#Merging of two sorted array.
left=[1,2,3,4]
right=[1,1,3,4,5,6,7]
def merge(left,right):
    result=[]
    a=len(left)
    b=len(right)
    i=j=0
    while i<a or j<b:
          if i<a and j<b:
             if left[i]> right[j]:
                result.append(right[j])
                j+=1
             else:
                result.append(left[i])
                i+=1
          else:
              if a>i:
                 result.append(left[i])
                 i+=1
              else:
                  result.append(right[j])
                  j+=1
    
    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_sort=arr[:mid]
    right_sort=arr[mid:]
    left=merge_sort(left_sort)
    right=merge_sort(right_sort)
    return merge(left,right)
print(merge_sort([1,4,3,6,5,7,8,5]))
#Here time comp is O(N*log2(N)). and space comp is O(N+log(N)) almost equal to O(log(N)).

