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
    
    def findNth(self, position):
        temp = self.head
        count = 0

        while(temp is not None):
            if (count == position):
                return temp.data
            count += 1
            temp = temp.next

if __name__ == '__main__':
    l = LinkedList()

    l.push(2)
    l.push(3)
    l.push(4)
    l.push(9)

    print(l.findNth(3))
        