class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def Reverse(head):
    if head is None or head.next is None:
        return
    cur = None
    next = None
    cur = head.next.next
    head = None
    while cur:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next


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
