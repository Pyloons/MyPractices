import math
def radix_sort(lists, radix=10):
    # k是序列中最大的数，以10为底取对数后取整的结果
    # 这里重复使用了int，因为ceil本来就是向上取整，再用int多此一举
    k = int(math.ceil(math.log(max(lists), radix)))
    # 准备十个鸡排桶
    bucket = [[] for _ in range(radix)]
    
    for i in range(1, k+1):
        # 这两个循环应该是鸡排的核心
        for j in lists:
            bucket[j//(radix**(i-1))%(radix**i)].append(j)
        # 港真我是第一次看见Python的语法里居然还要del语句
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists

if __name__ == "__main__":
    lists = [3,4,2,8,9,5,1]
    for i in lists:
        print(i, end=' ')
    print('')
    for i in radix_sort(lists):
        print(i, end=' ')
    print('')