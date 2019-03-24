call_count = 0
no_change_count = 0

def adjust_heap(lists, i, size):
    global call_count, no_change_count
    call_count += 1
    '''
    调整堆
    需要知道堆存在的列表，当前根节点下标和一个size参数
    与经典方式有所不同，这个算法每层递归仅能调整三个节点之间的关系
    即，递归深度最多为2
    '''
    # maxs是指父节点下标
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    maxs = i
    if i < size / 2:
        # 如果左子节点没有越界，并且比父节点大，父节点下标更新为左子结点下标
        if lchild < size and lists[lchild] > lists[maxs]:
            maxs = lchild
        # 类似左子节点
        if rchild < size and lists[rchild] > lists[maxs]:
            maxs = rchild
        # 如果确实父节点下标发生了改变，那么这个新下标所指的元素必须升上来
        if maxs != i:
            # 交换值实现上升
            lists[maxs], lists[i] = lists[i], lists[maxs]
            # 递归在maxs所指元素继续适应，看应不应该继续上升结点
            adjust_heap(lists, maxs, size)
        else:
            no_change_count += 1

def build_heap(lists, size):
    '''
    构建堆
    需要知道列表及其长度
    '''

    # 将前一半的元素进行调整，使之成堆
    # 之所以是前一半的元素，是因为完全二叉树的叶子节点数量要么等于非叶节点，要么比非叶多一个
    # 逆序则保证从堆底部最后一个元素开始调整
    # 经过维护，可以保证避免判断子节点到底是叶子节点还是空
    for i in range(0, (size//2))[::-1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    '''
    堆排序主体
    '''
    size = len(lists)
    build_heap(lists, size)
    # 从最后一个元素开始不断维护堆
    # 由于非叶结点都已经符合堆定义，所以叶节点调整就有了基础
    # 可以经过测试得到在整个算法完成时
    # 有效调整次数 = 总调整次数 - 未调整调用次数 = 2 × 数组长度 + 1
    # 正好符合叶子节点和非叶节点之间的数量关系
    # 之所以从下往上在排一遍是因为重新向上调整之后，原来的堆可能发生改变
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)

if __name__ == "__main__":
    # 经实际测试，其运算复杂度比nln(n)要大，但是远小于n^2
    # 手动敲Python shell估计其接近nlog3(n)
    lists = [3,4,2,8,9,5,1]
    for i in lists:
        print(i, end=' ')
    print('')
    heap_sort(lists)
    for i in lists:
        print(i, end=" ")
    print('')
    print(len(lists), call_count, no_change_count)

    lists = [3,4,2,3,4,2,8,9,5,3,4,2,8,9,5,8,9,5,1]
    for i in lists:
        print(i, end=' ')
    print('')
    heap_sort(lists)
    for i in lists:
        print(i, end=" ")
    print('')
    print(len(lists), call_count, no_change_count)
