def sum_items(l):
    if not l:
        return 0
    else:
        return 1 + sum_items(l[1:])

if __name__ == "__main__":
    print(sum_items([2,3,5]))
    print(sum_items([2,3,5,3,5,3,5,3,5,3,5,3,5]))
    print(sum_items([2,3,5,3,5,3,5,3,5,3,5,3,5,3,5]))