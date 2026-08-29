#Ques Building max-heap from array.


arr = [1,8,7,16,11,12,2,4]
n = len(arr)


def heapfiyDown(arr, ind):
    
    n = len(arr)
    
    largest_ind = ind
    
    leftchild_ind = 2*ind+1
    rightchild_ind = 2*ind+2
    
    #If leftchild hold largest value , update largest index.
    
    if leftchild_ind< n and arr[leftchild_ind]> arr[largest_ind]:
        largest_ind = leftchild_ind
        
    #If rightchild hold largest value , update largest index.
    if rightchild_ind< n and arr[rightchild_ind] > arr[largest_ind]:
        largest_ind = rightchild_ind
        
    #If largest is not the current ind , swap and heapfiy down.
        
    if largest_ind!= ind:
        arr[largest_ind],arr[ind] = arr[ind], arr[largest_ind]
        heapfiyDown(arr,largest_ind)
        

for i in range(n//2 -1,-1,-1):
    heapfiyDown(arr,i)
print(arr)

#Here time comp is O(N) not O(N/2 *logN).