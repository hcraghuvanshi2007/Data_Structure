# linked list 

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1️⃣ Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2️⃣ Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 3️⃣ Insert at given position (1-based index)
    def insert_position(self, position, data):
        if position == 1:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(position - 2):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4️⃣ Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # 5️⃣ Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    # ⭐ NEW: Delete at position p
    def delete_position(self, position):

        if self.head is None:
            print("List is empty")
            return

        # delete first node
        if position == 1:
            self.head = self.head.next
            return

        temp = self.head

        # move to (position-1) node
        for _ in range(position - 2):
            if temp is None or temp.next is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid Position")
            return

        # skip node
        temp.next = temp.next.next

    # 6️⃣ Search element
    def search(self, key):
        temp = self.head
        position = 1

        while temp:
            if temp.data == key:
                print(f"Element found at position {position}")
                return
            temp = temp.next
            position += 1

        print("Element not found")

    # 7️⃣ Display / Traversal linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
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


