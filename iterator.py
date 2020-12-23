class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def __iter__(self):
        return self.head

    def __next__(self):
        node = self.head
        nxt = node.next
        if nxt.next:
            self.head = nxt
            return node.val
        raise StopIteration

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        cur = self.head
        new = Node(val)
        if cur is not None:
            cur.prev = new
        new.next = cur
        self.head = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: return None
        cur = self.head
        new = Node(val)
        if index == 0:
            self.addAtHead(val)
        else:
            for i in range(index - 1):
                cur = cur.next
            new.next = cur.next
            cur.next = new
            new.prev = cur
            if new.next:
                new.next.prev = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return None
        cur = self.head
        if index == 0:
            self.head = cur.next
            if cur.next:
                cur.next.prev = None
        else:
            for i in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
            if cur.next:
                cur.next.prev = cur
        self.size -= 1


class Printer:
    def __init__(self, node):
        self.node = node

    def __next__(self):
        if not self.node:
            raise StopIteration
        else:
            node = self.node
            self.node = self.node.next
            return node.val

    def __iter__(self):
        return self


def main():
    lst = MyLinkedList()
    lst.addAtHead(1)
    lst.addAtHead(2)
    lst.addAtHead(3)
    lst.addAtTail(4)
    lst.addAtTail(5)
    lst.addAtIndex(2, 8)
    lst.addAtIndex(4, 9)
    lst.deleteAtIndex(1)
    printer = Printer(lst.head)
    for i in printer:
        print(i, ' ')
    print("------")
    print(next(lst))
    print(next(lst))


if __name__ == "__main__":
    main()
