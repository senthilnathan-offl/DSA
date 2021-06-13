class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def removeDuplicates(self, head):
        while self.head is None or self.head.next is None:
            return head

        hash = set()
        current = head
        hash.add(self.head.data)

        while (current.next is not None):
            if (current.next.data in hash):
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
        return head

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    l = LinkedList()

    l.push(8)
    l.push(9)
    l.push(7)
    l.push(9)
    l.push(7)
    l.push(1)
    l.push(8)

    print("Before..")
    l.printList()

    print("After..")
    l.removeDuplicates(l.head)
    l.printList()
