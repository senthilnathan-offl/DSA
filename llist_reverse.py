class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def reverseList(self):
        current = self.head
        prev = None
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    l = LinkedList()

    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(5)
    print("Before Reverse \n")
    l.printList()
    l.reverseList()
    print("After Reverse")
    l.printList()
