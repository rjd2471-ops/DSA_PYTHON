def minWindow( s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t)> len(s):
            return ""

        d1 = {}
        for j in t:
            d1[j] = d1.get(j,0)+1

        d2 = {}
        for k in s[:len(t)]:
            d2[k] = d2.get(k,0)+1
        if d1 == d2:
            return s[:len(t)]
        i = 0
        min_slide = ""
        for l in range(len(t),len(s)):
            d2[s[l]] = d2.get(s[l],0)+1

            while all(d2.get(char, 0) >= count for char, count in d1.items()):
                if len(min_slide) == 0 or  len(s[i:l+1])  < len(min_slide):
                    min_slide =   s[i:l+1]
                    
                d2[s[i]] -=1
                if d2[s[i]] == 0:
                    del d2[s[i]]
                i+=1

            
            
            
        return min_slide    
