def find_max(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l[0]
    else:
        may_max = find_max(l[1:])
        return l[0] if l[0] > may_max else may_max

if __name__ == "__main__":
    print(find_max([1,2,3,4,5,4,3,2,1]))
    print(find_max([1,2,3,4,5,4,3,2,11]))
    print(find_max([1,2,63,4,5,4,3,2,11]))
    print(find_max([1,1,1,1,1,1,1]))
    print(find_max([]))
    print(find_max([3,2,]))