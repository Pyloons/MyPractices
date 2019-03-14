def singleNumber(nums):
    p = 0
    l=sorted(nums)    # 这里就决定了整个函数的效率
    for _ in range(0, len(l)):  # 而排序不管怎么着，永远不会到O(logn)
        if p+1 == len(l) or l[p] != l[p+1]:
            return l[p]
        l = l[2:]

'''
# 刚开始没有理解^这种计算方法
# 后来在python shell里试了一下
# 发现异或计算的两个数如果相等，那么结果肯定为0
# 如果出现了形如a,a,b,c,c这种形式，那么肯定等于b

int singleNumber(A) {
    result = 0;
    length = len(A)
    for _ in range(0, length
        result ^=A[i]
    return result;
'''
