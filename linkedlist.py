class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class LinkedList:
    def __int__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    linklist = LinkedList()

    linklist.head = Node(1)
    second = Node(2)
    third = Node(3)

    linklist.head.next = second
    second.next = third
    third.next = None

    linklist.printList()
