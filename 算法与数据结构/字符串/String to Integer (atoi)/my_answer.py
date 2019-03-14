class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        
        if (re.match("\D*[a-zA-Z\.]|\s*(\+|\-)(\+|\-)+.*|.*(\+|\-)+\s+.*", str)):
            return 0
        num_line = re.search("[+-]?[0-9]+(\.?\d+)?", str)
        result = int(float(num_line.group())) if num_line else 0
        result = result if result < INT_MAX else INT_MAX
        result = result if result > INT_MIN else INT_MIN
        return result
