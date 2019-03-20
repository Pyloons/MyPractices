def sum(l):
    if not l:
        return 0
    else:
        return l[0] + sum(l[1:])

if __name__ == "__main__":
    print(sum([2,4,6]))
    print(sum([21,44,62]))
    print(sum([432,664,326]))
