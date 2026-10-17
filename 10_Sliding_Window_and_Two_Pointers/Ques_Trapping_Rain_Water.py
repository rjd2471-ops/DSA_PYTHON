class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        n = len(height)
        maxi = 0 
        water = 0
        j = n-1
        maxj = 0
        while i<j:
            if height[i]<= height[j]:
                maxi = max(maxi,height[i])
                water+= maxi-height[i]
                i+=1
            else:
                maxj = max(maxj,height[j])
                water += maxj-height[j]
                j-=1
        return water