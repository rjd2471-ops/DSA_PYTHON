#Concept Heapfiy Algrothim.

arr= [10,7,6,4,5,4,5,3,2]


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
heapfiyDown(arr,len(arr)-1)
print(arr)

def heapfiyUp(arr,ind):
    parent_ind = (ind-1)//2
    
    if ind>0 and arr[ind] > arr[parent_ind] :
        arr[ind],arr[parent_ind]= arr[parent_ind],arr[ind]
        heapfiyUp(arr,parent_ind)
        
        
#Here time comp is O(Log2N). and space comp stack space O(log2N).