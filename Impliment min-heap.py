#Impliment min-heap.


class Solution:
    def __init__(self,):
        self.arr = []
        self.count =0
        
    def heapifyUp(self,arr,ind):
        parentInd = (ind-1)//2
        
        if ind>0 and arr[ind] < arr[parentInd]:
            arr[ind],arr[parentInd] = arr[parentInd],arr[ind]
            self.heapifyUp(arr,parentInd)
            
    def heapifyDown(self,arr,ind):
        n= len(arr)
        
        smallestInd = ind
        
        leftchildInd = 2*ind+1
        rightchildInd = 2*ind+2
        
        if leftchildInd< n and arr[leftchildInd]< arr[smallestInd]:
            smallestInd = leftchildInd
            
        if rightchildInd< n and arr[rightchildInd]< arr[smallestInd]:
            smallestInd = rightchildInd
            
        if smallestInd!= ind:
            arr[smallestInd], arr[ind] = arr[ind], arr[smallestInd]
            self.heapifyDown(arr,smallestInd)
            
            
        
    def initializeheap(self):
        self.arr.clear()
        self.count = 0
        
    def insert(self,key):
        self.arr.append(key)
        self.heapifyUp(self.arr,self.count)
        self.count+=1
        
    def changekey(self,index, new_val):
       if self.arr[index] > new_val:
            self.arr[index] = new_val
            self.heapifyUp(self.arr,index)
            
        else:
            self.arr[index] = new_val
            self.heapifyDown(self.arr,index)
            
    def extractMin(self):
        if self.count == 0:
            return None
        
        ele = self.arr[0]
        self.arr[0],self.arr[self.count-1] = self.arr[self.count-1],self.arr[0]
        self.arr.pop()
        self.count-=1
        
        if self.count>0:
            self.heapifyDown(self.arr,0)
        return ele
    def isEmpty(self):
        return self.count==0
    
    def getMin(self):
        return self.arr[0] if self.count>0 else None
    
    
    def heapsize(self):
        return self.count
    
    