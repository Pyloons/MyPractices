class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        
        for i in s:
            if i in counter.keys():
                counter[i] += 1
            else:
                counter[i] = 1
                
        for j in s:
            if counter[j] == 1:
                return s.index(j)
            
        return -1
        