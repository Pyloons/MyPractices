def birecur(l, t):
    if len(l) == 0:
        return None
    if l[len(l)//2] == t:
        return t
    elif l[len(l)//2] < t:
        return birecur(l[len(l)//2:], t)
    elif t < l[len(l)//2]:
        return birecur(l[:len(l)//2], t)

if __name__ == "__main__":
    print(birecur([x for x in range(10)], 6))
