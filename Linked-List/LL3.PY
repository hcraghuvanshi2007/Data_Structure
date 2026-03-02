# Circular Singly Linked List

# Node class
class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1️⃣ Insert at beginning
    def insert_beginning(self, data):
        new_node = CircularNode(data)

        # empty list
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        # move to last node
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # 2️⃣ Insert at end
    def insert_end(self, data):
        new_node = CircularNode(data)

        # empty list
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # 3️⃣ Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        # only one node
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        # move to last node
        while temp.next != self.head:
            temp = temp.next

        self.head = self.head.next
        temp.next = self.head

    # 4️⃣ Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        # only one node
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        # move to second last node
        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

    # 5️⃣ Display circular linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            # stop after one full cycle
            if temp == self.head:
                break

        print("(back to head)")
        

# ---------------- MAIN PROGRAM ----------------
cll = CircularLinkedList()

cll.insert_beginning(10)
cll.insert_end(20)
cll.insert_end(30)
cll.insert_beginning(5)

print("Circular List:")
cll.display()

cll.delete_beginning()
cll.delete_end()

print("After Deletion:")
cll.display()