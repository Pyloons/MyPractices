class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

# 假设该链表带头结点

def Reverse(head):
    if head == None or head.next == None:
        return
    pre = None
    cur = None
    next = None

    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next

    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    cur.next = pre
    head.next = cur

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

