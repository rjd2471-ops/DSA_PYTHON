arr= [10,7,6,4,5,4,5,3,2]

def heapfiyDown(arr,ind):
    n = len(arr)
    
    smallest_ind = ind
    
    leftchild_ind = 2*ind+1
    rightchild_ind = 2*ind+2
    
    #If leftchild hold smallest value , update smallest index.
    
    if leftchild_ind< n and arr[leftchild_ind]< arr[smallest_ind]:
        smallest_ind = leftchild_ind
        
    #If rightchild hold smallest value , update smallest index.
    if rightchild_ind< n and arr[rightchild_ind] < arr[smallest_ind]:
        smallest_ind = rightchild_ind
        
    #If smallest is not the current ind , swap and heapfiy down.
        
    if smallest_ind!= ind:
        arr[smallest_ind],arr[ind] = arr[ind], arr[smallest_ind]
        heapfiyDown(arr,smallest_ind)

# Build Min Heap
n = len(arr)

for i in range(n // 2 - 1, -1, -1):
    heapfiyDown(arr, i)

print(arr)
#Here the time comp is O(N).

def heapfiyUp(arr,ind):
    parent_ind = (ind-1)//2
    
    if ind>0 and arr[ind] < arr[parent_ind] :
        arr[ind],arr[parent_ind]= arr[parent_ind],arr[ind]
        heapfiyUp(arr,parent_ind)
        
arr= [10,7,6,4,5,4,5,3,2]
n = len(arr)

for i in range(n):
    heapfiyUp(arr,i)
print(arr)
#Here time comp is O(N*logN).
