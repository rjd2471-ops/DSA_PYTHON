class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i,0)+1
        # d = sorted(d.items(), key = lambda x : x[1],reverse = True)
        
        # result = []
        # for key,val in d:
        #     if len(result)>=k:
        #         return result
        #     result.append(key)
        
        # return result
        #Here time comp is O(NlogN)
#-----------------------------------------------------------------------------------------------------------------------
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i,0)+1

        # import heapq
        # result = []
        # for key,val in d.items():
        #     if len(result) <k:
        #        heapq.heappush(result,(val,key))
        #     else:
        #         if result[0][0] < val:
        #             heapq.heappop(result)
        #             heapq.heappush(result,(val,key))
        # l = []
        # for i in result:
        #     l.append(i[1])
        # return l
        #Here time comp is O(NlogK)
#----------------------------------------------------------------------------------------------------------
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1

        bucket = [[] for _ in range(len(nums)+1)]    
        for key,val in d.items():
            bucket[val].append(key)  
        r = []
        for i in range(len(bucket)-1,-1,-1)  :
            if k<=0:
                return r
            if bucket[i] == []:
                continue
            r+=bucket[i]
            k-=len(bucket[i])
        #here time comp is O(N)

        

        
