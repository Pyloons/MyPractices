class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None


def RecursiveReverse(head):
    if head is None or head.next is None:
        return head
    else:
        newhead = RecursiveReverse(head.next)
        head.next.next = head
        head.next = None
    return newhead

def Reverse(head):
    if head is None:
        return
    firstNode = head.next
    newhead = RecursiveReverse(firstNode)
    head.next = newhead
    return newhead


if __name__ == "__main__":
    i = 1

    head = LNode(0)
    head.next = None
    tmp = None
    cur = head

    while i<8:
        tmp = LNode(0)
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print('before', end=' ')
    cur = head.next
    while cur:
        print(cur.data, end=' ')
        cur = cur.next

    print('\nafter', end=' ')
    Reverse(head)
    cur = head.next
    while cur:
        print(cur.data, end=' ')
        cur = cur.next
    print('')

