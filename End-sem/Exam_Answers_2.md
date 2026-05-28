# Data Structures Mock Test - Exam Answers (Part B)

## Q2
### a) Explain singly linked list also mention the advantage of Linked List over Array.
**Singly Linked List:** A singly linked list is a linear, dynamic data structure consisting of a sequence of elements called nodes. Each node contains two parts:
1. **Data:** The actual value or information.
2. **Next Pointer:** A reference (or link) to the next node in the sequence. The last node's pointer is set to `Null` (or `None`).

**Advantages over Array:**
*   **Dynamic Data Structure:** Linked lists can grow and shrink in size during runtime, allocating and deallocating memory dynamically. Arrays have a fixed, static size.
*   **Efficient Insertion and Deletion:** Inserting or deleting a node anywhere in a linked list is very fast ($O(1)$ if the position is known) because it only requires updating a couple of pointers. In an array, insertions and deletions (especially at the beginning or middle) require shifting all subsequent elements, taking $O(n)$ time.
*   **No Memory Wastage:** Memory is allocated precisely as needed when a new node is created. Arrays often have unused allocated memory if the array is not completely filled.

### b) Write a program in Python to implement a Singly Linked List with operations:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # i) Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # ii) Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # iii) Display all Nodes
    def display(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Usage Example:
# ll = SinglyLinkedList()
# ll.insert_at_end(10)
# ll.insert_at_beginning(5)
# ll.display() # Output: 5 -> 10 -> None
```

---
### OR (Q2)
### a) Explain all Types of Graphs like cyclic, Acyclic, Directed, Undirected, weighted, unweighted with neat and clear Diagram.
*(Note: Diagrams represented via text representation)*
*   **Directed Graph:** Edges have a specific direction, represented by arrows. (e.g., `A -> B` means you can go from A to B, but not necessarily B to A).
*   **Undirected Graph:** Edges have no direction. The connection is bi-directional. (e.g., `A -- B` means you can go from A to B and B to A).
*   **Cyclic Graph:** A graph that contains at least one cycle (a path that starts and ends at the same vertex). e.g., `A -> B -> C -> A`.
*   **Acyclic Graph:** A graph with absolutely no cycles. A Directed Acyclic Graph (DAG) is a common example. Trees are also acyclic undirected graphs.
*   **Weighted Graph:** Every edge has an associated weight or cost (e.g., distance between two cities). represented as `A --(5)-- B`.
*   **Unweighted Graph:** Edges have no weight (or all have a uniform weight of 1). It just shows whether a connection exists or not.

### b) Write algorithm of BFS traversal.
**Breadth-First Search (BFS) Algorithm:**
1. Create a `Queue` to keep track of nodes to visit.
2. Create a `Visited` set/list to keep track of nodes already visited.
3. Enqueue the starting node into the `Queue` and mark it as `Visited`.
4. Loop while the `Queue` is not empty:
   1. Dequeue a node from the front of the `Queue` and process/print it.
   2. For every adjacent neighbor of the dequeued node:
      * If the neighbor has not been `Visited`:
        1. Mark the neighbor as `Visited`.
        2. Enqueue the neighbor into the `Queue`.

---

## Q3
### a) What is a Queue? Explain its working with a neat and labeled diagram.
**Queue:** A Queue is a linear data structure that operates on the **First In, First Out (FIFO)** principle. This means the first element added to the queue will be the first one to be removed (like a line of people waiting for a ticket).

**Working:**
*   **Enqueue:** Adding an element. Elements are strictly added at the **Rear** (or Tail) end of the queue.
*   **Dequeue:** Removing an element. Elements are strictly removed from the **Front** (or Head) end of the queue.

*Diagram Representation:*
```text
  Dequeue (Remove) <--- [ Front | Element | Element | Rear ] <--- Enqueue (Insert)
```

### b) Implement a Stack using Python class and array. Your implementation should include Push and Pop.
```python
class Stack:
    def __init__(self):
        # Using a Python list as the underlying array structure
        self.stack_array = []

    # i) Push operation
    def push(self, data):
        self.stack_array.append(data)
        print(f"Pushed: {data}")

    # ii) Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from empty stack.")
            return None
        return self.stack_array.pop()

    def is_empty(self):
        return len(self.stack_array) == 0
```

---
### OR (Q3)
### a) Define Data Structure and Abstract Data Type (ADT). Explain the need of data structures In real-world Applications.
*   **Data Structure:** A concrete implementation of organizing, managing, and storing data in computer memory so it can be accessed and modified efficiently. (e.g., Arrays, Linked Lists).
*   **Abstract Data Type (ADT):** A logical, mathematical model of a data type. It defines *what* operations can be performed (like push/pop for a stack) but does not specify *how* they are implemented under the hood.
*   **Need in Real-World Applications:**
    *   **Data Management:** Handling massive datasets efficiently (e.g., databases using B-Trees).
    *   **Speed:** Fast searching and sorting algorithms depend on structures like Hash Tables or Heaps.
    *   **Resource Management:** Operating systems use Queues for task scheduling and Stacks for function call memory management.
    *   **Networking:** Graphs are heavily used in routing algorithms (e.g., Google Maps finding the shortest path).

### b) Differentiate between Static and Dynamic data structures with examples.
*   **Static Data Structures:** Memory size is fixed and allocated at compile time. 
    *   *Advantage:* Faster access (random access).
    *   *Disadvantage:* Memory size cannot be changed at runtime; can lead to overflow or wasted memory.
    *   *Example:* **Array** (size must be declared upfront in languages like C/Java).
*   **Dynamic Data Structures:** Memory size can grow or shrink at runtime dynamically as needed.
    *   *Advantage:* Highly flexible memory usage; no memory wastage.
    *   *Disadvantage:* Generally slower access (no random access, must traverse) and extra memory overhead for pointers.
    *   *Example:* **Linked List**.

---

## Q4
### a) What is a Tree? Explain basic tree terminologies such as root, height, leaf, and subtree.
**Tree:** A non-linear, hierarchical data structure that consists of nodes connected by edges, simulating a tree structure with a top-down approach. It contains no cycles.

**Terminologies:**
*   **Root:** The absolute topmost node of the tree. It has no parent.
*   **Height:** The length of the longest path from the root node down to a leaf node. (Number of edges).
*   **Leaf:** A node that has no children (the bottom-most nodes).
*   **Subtree:** Any node of the tree along with all of its descendants forms a subtree (a smaller tree within the larger tree).

### b) Explain the difference between Binary Tree and Binary Search Tree traversal.
*   **Binary Tree Traversal:** (Inorder, Preorder, Postorder). When traversing a standard Binary Tree, the output sequence of nodes is just the structural order of the tree. There is no mathematical ordering or guarantee about the values printed.
*   **Binary Search Tree (BST) Traversal:** A BST has a strict property: `Left Child < Root < Right Child`. Because of this property, if you perform an **Inorder Traversal** on a Binary Search Tree, the resulting output will always be sorted in **ascending order**.

---
### OR (Q4)
### a) What is a Graph data structure? Explain directed and undirected graph with a neat and labeled graph.
**Graph:** A non-linear data structure consisting of a finite set of **Vertices** (or nodes) and a set of **Edges** which connect pairs of vertices.

*   **Directed Graph (Digraph):** Edges have a specific direction indicating a one-way relationship.
    ```text
    (A) ---> (B)    (Can travel A to B, but not B to A)
    ```
*   **Undirected Graph:** Edges lack direction, meaning the connection is two-way.
    ```text
    (A) ---- (B)    (Can travel A to B, AND B to A)
    ```

### b) Write algorithm for DFS traversal.
**Depth-First Search (DFS) Algorithm (Recursive):**
1. Define function `DFS(graph, current_node, visited)`.
2. If `current_node` is not in `visited` set:
   1. Mark `current_node` as visited.
   2. Print or process `current_node`.
   3. For every adjacent neighbor of `current_node` in the graph:
      * Recursively call `DFS(graph, neighbor, visited)`.

---

## Q5
### a) Explain the logic of Insertion Sort with the help of a neat and clean diagram.
**Logic of Insertion Sort:**
Insertion sort works similarly to how you might sort playing cards in your hands. It splits the array into a "sorted" left part and an "unsorted" right part. It iterates through the unsorted part, picking one element at a time (the `key`), and places it into its exact correct position within the sorted left part by shifting larger elements to the right.

*Diagram/Trace:*
Array: `[4, 3, 2, 10]`
1. (Key=3): Compare 3 with 4. 4 > 3, so shift 4 right. Insert 3. -> `[3, 4, 2, 10]`
2. (Key=2): Compare 2 with 4, shift 4. Compare 2 with 3, shift 3. Insert 2. -> `[2, 3, 4, 10]`
3. (Key=10): Compare 10 with 4. 10 > 4, no shift needed. -> `[2, 3, 4, 10]` (Sorted)

### b) Write the code for the Insertion Sort
```python
def insertion_sort(arr):
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key, 
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr
```

---
### OR (Q5)
### a) Explain the work of Linear Search and time complexity of all scenarios and with the help of neat and clean diagram.
**Working of Linear Search:**
Linear search sequentially checks each element in an array/list starting from the very first index and moving to the last, until the target element is found or the end of the list is reached. It does not require the array to be sorted.

*Diagram:*
Target = 7. Array: `[2, 4, 6, 7, 9]`
- Check index 0 (2): No match.
- Check index 1 (4): No match.
- Check index 2 (6): No match.
- Check index 3 (7): Match found! Return index 3.

**Time Complexity Scenarios:**
*   **Best Case:** $O(1)$. The target element is found exactly at the first index (index 0).
*   **Average Case:** $O(n)$. The target is found somewhere in the middle. We check about $n/2$ elements.
*   **Worst Case:** $O(n)$. The target is found at the very last index, or the target does not exist in the array at all, meaning we must check every single element.

### b) Write the code for Binary Search.
```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
            
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
            
        # If target is smaller, ignore right half
        else:
            high = mid - 1
            
    # Target was not found
    return -1
```
