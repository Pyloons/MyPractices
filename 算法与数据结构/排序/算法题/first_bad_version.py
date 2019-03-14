BAD_VERSION = 0
def isBadVersion(n):
    if n > BAD_VERSION:
        return True
    return False

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        
        left = 1
        right = n
        
        while left < right:
            mid = (right + left) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    right = mid
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    left = mid + 1
        return None
