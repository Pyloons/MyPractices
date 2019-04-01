'''
415. Add Strings
Easy

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

class MySolution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums = '0123456789'
        int_nums1 = [x for x in num1]
        int_nums2 = [x for x in num2]
        for_sum1 = 0
        for_sum2 = 0
        # 如果你说index方法也不能用，那我写个循环去数也是一样的，这样毫无意义
        for i in int_nums1:
            for_sum1 = 10 * for_sum1 + nums.index(i)
        for i in int_nums2:
            for_sum2 = 10 * for_sum2 + nums.index(i)
        
        return str(for_sum1 + for_sum2)