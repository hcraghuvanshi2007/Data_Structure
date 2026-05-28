# linked list 

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.address = None


# Linked List class
class SinglyLinkedList:
    def __init__(self):
        sh = None

    # 1️⃣ Insert at beginning
    def insert_beginning(self, data):
        nN = Node(data)
        nN.address = sh
        sh = nN

    # 2️⃣ Insert at end
    def insert_end(self, data):
        nN = Node(data)

        if sh is None:
            sh = nN
            return

        cN = sh
        while cN.address!= None:
            cN = cN.address
            
        cN.address = nN

    # 3️⃣ Insert at given position (1-based index)
    def insert_position(self, position, data):
        if position == 1:
            self.insert_beginning(data)
            return

        nN = Node(data)
        cN = sh

        for _ in range(position - 2):
            if cN is None:
                print("Invalid Position")
                return
            cN = cN.address

        if cN is None:
            print("Invalid Position")
            return

        nN.address = cN.address
        cN.address = nN

    # 4️⃣ Delete from beginning
    def delete_beginning(self):
        if sh is None:
            print("List is empty")
            return
        sh = sh.address

    # 5️⃣ Delete from end
    def delete_end(self):
        if sh is None:
            print("List is empty")
            return

        if sh.address is None:
            sh = None
            return

        cN = sh
        while cN.address.address:
            cN = cN.address

        cN.address = None

    # ⭐ NEW: Delete at position p
    def delete_position(self, position):

        if sh is None:
            print("List is empty")
            return

        # delete first node
        if position == 1:
            sh = sh.address
            return

        cN = sh

        # move to (position-1) node
        for _ in range(position - 2):
            if cN is None or cN.address is None:
                print("Invalid Position")
                return
            cN = cN.address

        if cN.address is None:
            print("Invalid Position")
            return

        # skip node
        cN.address = cN.address.address

    # 6️⃣ Search element
    def search(self, key):
        cN = sh
        position = 1

        while cN:
            if cN.data == key:
                print(f"Element found at position {position}")
                return
            cN = cN.address
            position += 1

        print("Element not found")

    # 7️⃣ Display / Traversal linked list
    def display(self):
        if sh is None:
            print("List is empty")
            return

        cN = sh
        while cN:
            print(cN.data, end=" -> ")
            cN = cN.address
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


