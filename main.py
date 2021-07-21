class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self): # tell python how to print this node
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # returns length of list
    def __len__(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return "[]"

        current = self.head
        result = str(current) # what we return once all nodes are concatenated
        while current.next:
            result += f" -> {str(current.next)}"
            current = current.next
        return f"[{result}]"

    def insert_front(self, data):
        if self.size == 0: #list is empty
            self.head = Node(data, None) # make new node the head
            self.tail = self.head # set tail to head
        elif self.size == 1:
            self.head = Node(data, self.tail)
        else:
            temp = self.head
            self.head = Node(data, temp)
        self.size += 1

    def insert_end(self, data):
        if self.size == 0:
            self.head = Node(data, None)
            self.tail = self.head
        else: 
            temp = self.tail
            self.tail = Node(data, None)
            temp.next = self.tail
        self.size += 1


myList = LinkedList()
myList.insert_front("Taylor")
myList.insert_front("Dave")
myList.insert_front("Anna")
myList.insert_end("King")

print(myList)
print(len(myList))
