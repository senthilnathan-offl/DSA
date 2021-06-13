

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAfter(self, prev_node, new_data):

        if prev_node == None:
            print("The Given Node should be valid")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next

        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
        else:
            last = self.head
            while(last.next):
                last = last.next

            last.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    third.next = None

    llist.insertAfter(llist.head.next.next, 9)
    llist.append(4)

    llist.printList()
