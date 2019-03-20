def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def select_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

if __name__ == "__main__":
    try_arrays = [
        [5, 3, 6, 2, 10],
        [3, 4, 2, 8, 9, 5, 1],
        [38, 65, 97, 76, 13, 27, 49]
    ]
    for arr in try_arrays:
        tmp_arr = arr[:]
        print("{} -> {}".format(tmp_arr, select_sort(arr)))
