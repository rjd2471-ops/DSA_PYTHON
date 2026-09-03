def kSmallestPairs(nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        result = []
        heap = []
        visited = set()

        heapq.heappush(heap,(nums1[0]+ nums2[0],0,0))
        visited.add((0,0))

        while k and heap :
            l,i,j = heapq.heappop(heap)
            result.append([nums1[i],nums2[j]])
            if i+1< len(nums1) and (i+1,j) not in visited:
                heapq.heappush(heap,(nums1[i+1]+ nums2[j],i+1,j))
                visited.add((i+1,j))

            if j+1< len(nums2) and (i,j+1) not in visited:
                heapq.heappush(heap,(nums1[i]+ nums2[j+1],i,j+1))
                visited.add((i,j+1))
            k-=1
        return result
        
print(kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
#_-------------------------------------------------------------------------------------------------
#The other approch for this questions is.


import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):

        result = []
        heap = []

        # Put the first pair from each row
        for i in range(min(k, len(nums1))):
            heapq.heappush(
                heap,
                (nums1[i] + nums2[0], i, 0)
            )

        while heap and k > 0:

            total, i, j = heapq.heappop(heap)

            result.append([nums1[i], nums2[j]])

            # Move right in the same row
            if j + 1 < len(nums2):
                heapq.heappush(
                    heap,
                    (nums1[i] + nums2[j + 1], i, j + 1)
                )

            k -= 1

        return result