
#Create node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
# Triển khai class linked list
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    # Insert a new node at the end of the list.
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.size += 1
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode
        self.size += 1
    #Insert a new node at the end of the list
    def insertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.size += 1
            return
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    #Insert a new node after the given node


    #Print the linked list
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end = " -> ")
            currentNode = currentNode.next
        print('None')
