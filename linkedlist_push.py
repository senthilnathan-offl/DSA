class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    third.next = None

    llist.push(0)
    llist.printList()