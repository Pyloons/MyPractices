def merge(left, right):
    i, j = 0, 0
    result = []
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)

if __name__ == "__main__":
    lists = [3,4,2,8,9,5,1]
    for i in lists:
        print(i, end=' ')
    print('')
    for i in merge_sort(lists):
        print(i, end=' ')
    print('')
