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
    
    def posDelete(self, pos):
        temp = self.head

        if (pos == 0):
            self.head = temp.next
            temp = None
            return
        else:
            for i in range(pos-1):
                temp = temp.next
                if temp == None:
                    break

            if (temp is None): 
                return
            if (temp.next is None):
                return
            
            next = temp.next.next

            temp.next = None
            temp.next = next

    def printList(self):
        temp = self.head

        while(temp is not None):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    l = LinkedList()
    l.head = Node(1)
    second = Node(2)
    third = Node(3)

    l.head.next = second
    second.next = third
    third.next = None

    l.push(9)
    l.push(7)

    l.posDelete(0)
    l.posDelete(1)
    l.printList()