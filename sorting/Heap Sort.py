# Heap Sort

arr = [1,4,7,6,10,9,11,9]

n = len(arr)

def heapifyDown(arr, ind, size):

    largest_ind = ind

    leftchild_ind = 2*ind + 1
    rightchild_ind = 2*ind + 2

    # Check left child
    if leftchild_ind < size and arr[leftchild_ind] > arr[largest_ind]:
        largest_ind = leftchild_ind

    # Check right child
    if rightchild_ind < size and arr[rightchild_ind] > arr[largest_ind]:
        largest_ind = rightchild_ind

    # Swap if needed
    if largest_ind != ind:
        arr[ind], arr[largest_ind] = arr[largest_ind], arr[ind]
        heapifyDown(arr, largest_ind, size)


# Step 1: Build Max Heap
for i in range(n//2 - 1, -1, -1):
    heapifyDown(arr, i, n)

# Step 2: Extract elements one by one
for last_index in range(n-1, 0, -1):
    arr[0], arr[last_index] = arr[last_index], arr[0]
    heapifyDown(arr, 0, last_index)

print(arr)
#Here time comp is O(N+NlogN).