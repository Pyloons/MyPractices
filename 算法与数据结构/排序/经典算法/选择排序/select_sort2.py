def select_sort2(lists):
    """
    不申请新列表，直接与目标位置元素交换
    """
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i+1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


if __name__ == "__main__":
    try_arrays = [
        [5, 3, 6, 2, 10],
        [3, 4, 2, 8, 9, 5, 1],
        [38, 65, 97, 76, 13, 27, 49]
    ]
    for arr in try_arrays:
        tmp_arr = arr[:]
        print("{} -> {}".format(tmp_arr, select_sort2(arr)))