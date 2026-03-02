# linked list 

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.address = None


# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1️⃣ Insert at beginning
    def insert_beginning(self, data):
        newNode = Node(data)
        newNode.address = self.head
        self.head = newNode

    # 2️⃣ Insert at end
    def insert_end(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        currentNode = self.head
        while currentNode.address!= None:
            currentNode = currentNode.address
            
        currentNode.address = newNode

    # 3️⃣ Insert at given position (1-based index)
    def insert_position(self, position, data):
        if position == 1:
            self.insert_beginning(data)
            return

        newNode = Node(data)
        currentNode = self.head

        for _ in range(position - 2):
            if currentNode is None:
                print("Invalid Position")
                return
            currentNode = currentNode.address

        if currentNode is None:
            print("Invalid Position")
            return

        newNode.address = currentNode.address
        currentNode.address = newNode

    # 4️⃣ Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.address

    # 5️⃣ Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.address is None:
            self.head = None
            return

        currentNode = self.head
        while currentNode.address.address:
            currentNode = currentNode.address

        currentNode.address = None

    # ⭐ NEW: Delete at position p
    def delete_position(self, position):

        if self.head is None:
            print("List is empty")
            return

        # delete first node
        if position == 1:
            self.head = self.head.address
            return

        currentNode = self.head

        # move to (position-1) node
        for _ in range(position - 2):
            if currentNode is None or currentNode.address is None:
                print("Invalid Position")
                return
            currentNode = currentNode.address

        if currentNode.address is None:
            print("Invalid Position")
            return

        # skip node
        currentNode.address = currentNode.address.address

    # 6️⃣ Search element
    def search(self, key):
        currentNode = self.head
        position = 1

        while currentNode:
            if currentNode.data == key:
                print(f"Element found at position {position}")
                return
            currentNode = currentNode.address
            position += 1

        print("Element not found")

    # 7️⃣ Display / Traversal linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.address
        print("None")


# ---------------- MAIN PROGRAM ----------------
ll = SinglyLinkedList()

ll.insert_beginning(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_position(2, 15)

ll.display()

ll.delete_beginning()
ll.delete_end()

ll.display()

# ⭐ delete node at position p
ll.delete_position(2)

ll.display()

ll.search(20)


