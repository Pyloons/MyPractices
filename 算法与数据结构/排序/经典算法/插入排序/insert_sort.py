def insert_sort(lists):
    count = len(lists)
    # 因为第一个元素自成有序序列，所以遍历从第二个元素开始
    for i in range(1, count):
        # 获取当前需要向前插入的元素
        key = lists[i]
        # 从i前面一个位置开始插入
        j = i - 1
        while j >= 0:
            # 如果待插位置的原有元素比待插元素大（如果是降序也可以是小）
            # 那么移动j元素到j+1位，j元素用待插元素替代
            # 这个过程简直是逆向的冒泡，但是被插入序列本身的有序性决定这次冒泡最多只需一次遍历
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

if __name__ == "__main__":
    lists = [3,4,2,8,9,5,1]
    for i in lists:
        print(i, end=' ')
    print('')
    for i in insert_sort(lists):
        print(i, end=' ')
    print('')
