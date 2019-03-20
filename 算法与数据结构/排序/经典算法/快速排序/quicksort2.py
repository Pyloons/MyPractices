def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        # 大概能懂这里是把列表一分为二，但是可读性绝对比不上切片
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left-1)
    quick_sort(lists, left+1, high)
    return lists

if __name__ == "__main__":
    lists = [3,4,2,8,9,5,1]
    print('排序前：', end='')
    for i in lists:
        print(i, end=' ')
    print('')
    print('排序后：', end='')
    for i in quick_sort(lists, 0, len(lists)-1):
        print(i, end=' ')
    print('')