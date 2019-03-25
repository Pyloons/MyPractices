def shell_sort(lists):
    count = len(lists)
    step = 2
    group = count // step
    # 确定好序列长度、分组步长和分组数量后开始排序
    # 这里变量名太差，group才是实际上的步长，或者说取数跨度
    while group > 0:
        # 这一层循环用来迭代每次循环步长序列的细化
        # 下方for循环的目的是操作到每一个组
        for i in range(0, group):
            # group本身确实既是步长序列每个元素之间的位置差
            # 也是代表了分组数量
            # j是某一个分组的第二个元素的实际下标
            j = i + group
            # 如果某个分组存在第二个元素，那么该分组一定存在，即可开始排序
            while j < count:
                # 但是排序不能从第二个元素开始，所以用k来回到第一个元素
                k = j - group
                print(k, group)
                # key则指向k所指元素的下一个元素
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        # 从这里k+group可以看出，group是事实步长
                        lists[k+group] = lists[k]
                        lists[k] = key
                    # k每次减少一个步长，说明k是待排元素的实际下标
                    # 而且这些元素是倒走着排序的
                    k -= group
                # j的增量是步长
                # j的步长会决定上面的k循环次数不断变化
                # 刚开始1次，然后2次……直到整个步长序列倒着走一遍
                j += group
        # 分组越来越细
        group //= step
    return lists

if __name__ == "__main__":
    lists = [3,4,2,8,9,5,1]
    for i in lists:
        print(i, end=' ')
    print('')
    for i in shell_sort(lists):
        print(i, end=' ')
    print('')
