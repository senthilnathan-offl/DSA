class Node:
    def __init__(self, data):
        self.data= data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def DeleteList(self):
        current = self.head
        while current:
            prev = current.next

            del current.data
            current = prev
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

if __name__ == '__main__':
    l = LinkedList()

    l.push(8)
    l.push(9)
    l.push(10)
    l.push(2)

    l.DeleteList()