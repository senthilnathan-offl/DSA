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

    def Delete(self, key):
        temp = self.head
        #traverse till the last Node
        while(temp is not None):
            #if head itself holds the key
            if (temp.data == key):
                #make the head node as the next node
                self.head = temp.next
                #free the memory
                temp = None
            else:
                while(temp is not None):
                    if (temp.data == key):
                        break
                    #store the value of previous node in prev variable.
                    prev = temp
                    temp = temp.next
                #if it is not return
                if (temp == None):
                    return
                #make the next of the previous variable as the next of key node.
                prev.next = temp.next

                temp = None

    def printList(self):
        temp = self.head
        
        while(temp is not None):
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

    llist.push(8)
    llist.Delete(8)
    llist.printList()
