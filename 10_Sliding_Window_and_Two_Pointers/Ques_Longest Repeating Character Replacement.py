class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {}

        i = 0
        max_count = 0
        max_freq = 0
        for j in range(len(s)):
            d[s[j]] = d.get(s[j],0)+1
            max_freq = max(max_freq,d[s[j]])
            while j-i+1 - max_freq > k:
                d[s[i]]-=1
                if d[s[i]] == 0:
                    del d[s[i]]
                i+=1
            
            max_count = max(j-i+1,max_count)
        return max_count

        