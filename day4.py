//create a linkedList

class Node:
    def __init__(self, data):
        self.data=data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head = None
    def addElement(self, element):
        newNode = Node(element)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode 
        else:
            self.head = newNode

linky = LinkedList()
linky.addElement(5)
print(linky.head.data)