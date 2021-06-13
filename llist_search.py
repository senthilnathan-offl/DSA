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

    def searchElem(self, elem):
        temp = self.head

        while (temp is not None):
            if (temp.data == elem):
                return True
            temp = temp.next
        else:
            return False


if __name__ == '__main__':
    l = LinkedList()

    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(5)

    if l.searchElem(1):
        print("Yes")
    else:
        print("No")
