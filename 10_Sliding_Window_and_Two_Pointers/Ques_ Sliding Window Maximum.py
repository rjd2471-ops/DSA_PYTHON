class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        result = []
        heap = []
        n = len(nums)
        if n<k:
            return []
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        result.append(-heap[0][0])

        for j in range(k,n):
            heapq.heappush(heap,(-nums[j],j))

            while heap[0][1] <= j-k:#if current max element is outside the window this gives this.
                heapq.heappop(heap)

            result.append(-heap[0][0])
        return result

#Here the time complexity is O(nlogk) because we are using heap and the space complexity is O(k) because we are storing k elements in the heap.