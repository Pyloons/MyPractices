def bubble_sort(lists):
    for i in range(len(lists)-1):
        for j in range(len(lists)-i-1):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]

    return lists

if __name__ == "__main__":
    lists=[3,4,2,8,9,5,1]
    for i in lists:
        print(i,end=' ')
    print('')
    for i in bubble_sort(lists):
        print(i,end=' ')
    print('')
