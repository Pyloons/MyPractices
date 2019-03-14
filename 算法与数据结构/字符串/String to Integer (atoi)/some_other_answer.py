import re
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        '''
        评论：最关键的是前面的^ *，这屏蔽了诸如“+-1”这种
        '''
        str = re.search(r"^ *[-+]?[0-9]+", str)
        if str:
            val=int(str.group())
            if val<INT_MIN:
                return INT_MIN
            elif val>INT_MAX:
                return INT_MAX
            else:
                return val
        return 0