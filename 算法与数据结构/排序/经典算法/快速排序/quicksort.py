def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array)//2]
        remain = array[:len(array)//2] + array[len(array)//2+1:]
        less = [i for i in remain if i <= pivot]
        greater = [i for i in remain if i > pivot]
        return quicksort(greater) + [pivot] + quicksort(less)

if __name__ == "__main__":
    print(quicksort([5,7,3,8,3,6,4,1]))