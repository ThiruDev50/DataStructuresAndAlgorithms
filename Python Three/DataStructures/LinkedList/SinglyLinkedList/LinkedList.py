class Node:
    def __init__(self, data):
        # When creating a node, we are assigning the data and its reference to Null
        # ie, it is pointing to None, and we can initalize some other prop of a node when creating
        self.data = data
        self.ref = None


class LinkedList:
    # While initalizing, we simply pointing the head of the list to None
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        head = self.head
        if (head is None):
            print("Linked list is empty")
            return
        while head.ref is not None:
            print(head.data, end="->")
            head = head.ref
        # While loop will break when ref is None, A Node's ref is null also have data
        print(head.data)

    def addLast(self, data):
        newNode = Node(data)
        if self.head is None:
            # List is empty so setting as first element
            self.head = newNode
        else:
            # Find the last node and assign its ref to the new node
            head = self.head
            while head.ref is not None:
                head = head.ref
            head.ref = newNode

    def addFirst(self, data):
        newNode = Node(data)
        if self.head is None:
            # List is empty so setting as first element
            self.head = newNode
        else:
            head = self.head  # Take the current head node
            newNode.ref = head  # Assign the ref of new node to the head
            self.head = newNode  # Assign the new node as head


linkedList = LinkedList()
linkedList.printLinkedList()
linkedList.addLast(23)
linkedList.addLast(33)
linkedList.addFirst(43)
linkedList.printLinkedList()
