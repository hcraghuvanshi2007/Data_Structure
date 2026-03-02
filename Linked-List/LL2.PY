# Doubly Linked List

# Node class
class DoublyNode:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1️⃣ Insert at beginning
    def insert_beginning(self, data):
        new_node = DoublyNode(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    # 2️⃣ Insert at end
    def insert_end(self, data):
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # 3️⃣ Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    # 4️⃣ Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # 5️⃣ Traverse forward
    def traverse_forward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # 6️⃣ Traverse backward
    def traverse_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # move to last node
        while temp.next:
            temp = temp.next

        # traverse backward
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# ---------------- MAIN PROGRAM ----------------
dll = DoublyLinkedList()

dll.insert_beginning(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_beginning(5)

print("Forward Traversal:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()

dll.delete_beginning()
dll.delete_end()

print("After Deletion:")
dll.traverse_forward()