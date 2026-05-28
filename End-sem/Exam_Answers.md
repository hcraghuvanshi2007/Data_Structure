# Data Structures Mock Test - Exam Answers

## PART - A

**Q1. Differentiate between Array and Linked List on the basis of Memory allocation and Insertion operation.**
*   **Memory Allocation:** Arrays have static, contiguous memory allocation (memory is allocated as a single block at compile/initialization time). Linked Lists have dynamic, non-contiguous memory allocation (nodes are created at runtime and scattered in memory).
*   **Insertion Operation:** In an Array, insertion is generally slow ($O(n)$) because elements may need to be shifted to accommodate a new element. In a Linked List, insertion is fast ($O(1)$ at a known position) as it only involves updating the pointers of the adjacent nodes.
*   **Code Example (Insertion):**
    ```python
    # Array Insertion at index i
    for k in range(n-1, i-1, -1):
        arr[k+1] = arr[k]  # Shifting elements right
    arr[i] = new_value
    
    # Linked List Insertion after a given node
    new_node = Node(new_value)
    new_node.next = prev_node.next
    prev_node.next = new_node
    ```

**Q2. Find the time complexity: `i = 1 while i <= n: i = i * 2`**
*   **Answer:** $O(\log_2 n)$.
*   **Explanation:** The variable `i` starts at 1 and doubles in each iteration ($1, 2, 4, 8, \dots, 2^k$). The loop terminates when $2^k > n$. Thus, the number of iterations $k$ is roughly $\log_2 n$, giving a time complexity of $O(\log n)$.

**Q3. State whether the following statement is TRUE or FALSE: “Binary Search can be applied on unsorted arrays.” Justify your answer.**
*   **FALSE**. Binary search inherently relies on the property that the elements are sorted. It works by checking the middle element and then eliminating half of the remaining elements based on whether the target is less than or greater than the middle element. This logic fails entirely if the array is unsorted.

**Q4. What is Stack Underflow?**
*   **Stack Underflow** is an error condition that occurs when you try to perform a `pop()` (delete) operation on a stack that is already empty.
    ```python
    def pop(stack):
        if len(stack) == 0:
            print("Stack Underflow")
            return None
        return stack.pop()
    ```

**Q5. Write the inorder traversal rule of a Binary Tree.**
*   **Rule:** 
    1. Recursively traverse the **Left** subtree.
    2. Visit the **Root** node.
    3. Recursively traverse the **Right** subtree.
    *(Left, Root, Right)*
*   **Algorithm (Pseudocode):**
    ```python
    def inorder(root):
        if root is not None:
            inorder(root.left)
            print(root.val)
            inorder(root.right)
    ```

**Q6. Differentiate between BFS and DFS.**
*   **BFS (Breadth-First Search):** Traverses a graph layer by layer (level by level). It uses a **Queue** data structure. Useful for finding the shortest path in unweighted graphs.
*   **DFS (Depth-First Search):** Explores a graph by going as deep as possible along each branch before backtracking. It uses a **Stack** data structure (or recursion). 

**Q7. What is the worst-case complexity of Quick Sort?**
*   **Answer:** $O(n^2)$. 
*   **Explanation:** This happens when the pivot selection consistently produces the most unbalanced partitions possible (e.g., picking the smallest or largest element as the pivot in a sorted or reverse-sorted array).

---

## PART - B

**Q1. Quick Sort Dry Run**
Array: `35, 10, 50, 25, 5, 40, 15` (Pivot: First Element)

*   **Pivot Selection & Partitioning Steps:**
    *   **Initial Array:** `[35, 10, 50, 25, 5, 40, 15]`, Pivot = `35`
    *   Elements < 35: `[10, 25, 5, 15]`
    *   Elements > 35: `[50, 40]`
    *   Array after partitioning: `[10, 25, 5, 15] 35 [50, 40]`
*   **Recursive Breakdown:**
    *   **Left Subarray:** `[10, 25, 5, 15]` -> Pivot = `10`
        *   Left (< 10): `[5]`, Right (> 10): `[25, 15]`
        *   Array becomes: `[5] 10 [25, 15]`
        *   **Right Sub-subarray:** `[25, 15]` -> Pivot = `25`
            *   Left (< 25): `[15]`, Right: `[]`
            *   Array becomes: `[15] 25`
        *   Sorted Left part: `[5, 10, 15, 25]`
    *   **Right Subarray:** `[50, 40]` -> Pivot = `50`
        *   Left (< 50): `[40]`, Right: `[]`
        *   Array becomes: `[40] 50`
        *   Sorted Right part: `[40, 50]`
*   **Final sorted array:** `5, 10, 15, 25, 35, 40, 50`
*   **Time complexity:** Average Case: $O(n \log n)$, Worst Case: $O(n^2)$
*   **Algorithm Implementation:**
    ```python
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    ```

**Q2. Queue Rearrangement**
Using queue operations (enqueue and dequeue) and assuming one auxiliary queue (`Aux_Q`), transform `[1 2 3 4 5 6]` into `[1 3 5 2 4 6]`.
Let original queue be `Q` (front is left).
*   **Step 1:** Dequeue 1 from `Q` and Enqueue it back to `Q`. -> `Q = [2, 3, 4, 5, 6, 1]`
*   **Step 2:** Dequeue 2 from `Q` and Enqueue it to `Aux_Q`. -> `Q = [3, 4, 5, 6, 1]`, `Aux_Q = [2]`
*   **Step 3:** Dequeue 3 from `Q` and Enqueue it back to `Q`. -> `Q = [4, 5, 6, 1, 3]`, `Aux_Q = [2]`
*   **Step 4:** Dequeue 4 from `Q` and Enqueue it to `Aux_Q`. -> `Q = [5, 6, 1, 3]`, `Aux_Q = [2, 4]`
*   **Step 5:** Dequeue 5 from `Q` and Enqueue it back to `Q`. -> `Q = [6, 1, 3, 5]`, `Aux_Q = [2, 4]`
*   **Step 6:** Dequeue 6 from `Q` and Enqueue it to `Aux_Q`. -> `Q = [1, 3, 5]`, `Aux_Q = [2, 4, 6]`
*   **Step 7:** Now enqueue all elements from `Aux_Q` into `Q`.
    *   Dequeue 2 from `Aux_Q`, Enqueue to `Q`. -> `Q = [1, 3, 5, 2]`
    *   Dequeue 4 from `Aux_Q`, Enqueue to `Q`. -> `Q = [1, 3, 5, 2, 4]`
    *   Dequeue 6 from `Aux_Q`, Enqueue to `Q`. -> `Q = [1, 3, 5, 2, 4, 6]`
*   **Final Queue:** `[1, 3, 5, 2, 4, 6]`
*   **Algorithm Implementation:**
    ```python
    from collections import deque
    
    Q = deque([1, 2, 3, 4, 5, 6])
    Aux_Q = deque()
    
    # Process original queue size elements
    for _ in range(3):
        Q.append(Q.popleft())        # Keep odd element
        Aux_Q.append(Q.popleft())    # Move even element to Aux_Q
        
    # Append back the extracted even elements
    while Aux_Q:
        Q.append(Aux_Q.popleft())
        
    # Result: Q is [1, 3, 5, 2, 4, 6]
    ```

**Q3. Stack Operations**
1.  **Show stack after every operation:**
    *   `push(10)` -> Stack: `[10]` (top is 10)
    *   `push(20)` -> Stack: `[10, 20]`
    *   `push(30)` -> Stack: `[10, 20, 30]`
    *   `pop()` -> Stack: `[10, 20]` (popped 30)
    *   `push(40)` -> Stack: `[10, 20, 40]`
    *   `pop()` -> Stack: `[10, 20]` (popped 40)
    *   `push(50)` -> Stack: `[10, 20, 50]`
2.  **What is the final stack?** `[10, 20, 50]`
3.  **What is the top element?** `50`
4.  **What happens if another pop operation is performed on an empty stack?** A "Stack Underflow" error occurs, indicating the stack has no elements left to remove.
*   **Algorithm Implementation:**
    ```python
    stack = []
    stack.append(10)  # push(10)
    stack.append(20)  # push(20)
    stack.append(30)  # push(30)
    stack.pop()       # pop() -> returns 30
    stack.append(40)  # push(40)
    stack.pop()       # pop() -> returns 40
    stack.append(50)  # push(50)
    # Final stack: [10, 20, 50]
    # Top element: stack[-1] -> 50
    ```

**Q4. Binary Tree Traversal**
```text
      A
     / \
    B   C
   / \   \
  D   E   F
```
1.  **Inorder (Left, Root, Right):** `D, B, E, A, C, F`
    *(Tracing: Left of A is subtree B. Inorder of B is D, B, E. Then root A. Right of A is subtree C. Inorder of C is C, F.)*
2.  **Preorder (Root, Left, Right):** `A, B, D, E, C, F`
    *(Tracing: Root A. Preorder of B is B, D, E. Preorder of C is C, F.)*
3.  **Postorder (Left, Right, Root):** `D, E, B, F, C, A`
    *(Tracing: Postorder of B is D, E, B. Postorder of C is F, C. Then root A.)*
*   **Algorithm Implementation:**
    ```python
    def preorder(node):
        if node:
            print(node.val, end=" ")
            preorder(node.left)
            preorder(node.right)
            
    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val, end=" ")
            inorder(node.right)
            
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            print(node.val, end=" ")
    ```

**Q5. BFS and DFS Traversal**
Given Edges: `A -> B, C`, `B -> D, E`, `C -> F`, `E -> G`. Start at A.
1.  **BFS Traversal (Breadth-First):** `A, B, C, D, E, F, G`
    *Tracing: Visit A. Neighbors of A: B, C. Visit B, C. Neighbors of B: D, E. Neighbors of C: F. Visit D, E, F. Neighbors of E: G. Visit G.*
2.  **DFS Traversal (Depth-First):** `A, B, D, E, G, C, F`
    *Tracing: Visit A, go to first neighbor B, go to first neighbor D (dead end), go back to B, go to next neighbor E, go to neighbor G (dead end). Backtrack to A, go to next neighbor C, go to neighbor F (dead end).*
**Also specify:**
*   Data structure used in BFS: **Queue**
*   Data structure used in DFS: **Stack** (or Recursion / Call Stack)
*   **Algorithm Implementation:**
    ```python
    # BFS implementation using Queue
    def bfs(graph, start):
        queue = [start]
        visited = set([start])
        while queue:
            node = queue.pop(0) # Dequeue front
            print(node, end=" ")
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
    # DFS implementation using Recursion (Implicit Stack)
    def dfs(graph, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(graph, neighbor, visited)
    ```

**Q6. Construct Binary Tree**
*   **Preorder:** `A B D E C F`
*   **Inorder:** `D B E A C F`
*   **Root identification:** The first element in Preorder traversal is always the root. Therefore, **A** is the root node.
*   **Left and Right Subtrees:** Find 'A' in the Inorder traversal. Elements to the left (`D B E`) belong to the Left subtree. Elements to the right (`C F`) belong to the Right subtree.
*   **Recursive subdivision:**
    *   Left subtree elements: `D B E` (Inorder), `B D E` (Preorder) -> Root is **B**. Left child is **D**, right child is **E**.
    *   Right subtree elements: `C F` (Inorder), `C F` (Preorder) -> Root is **C**. Left child is empty, right child is **F**.
*   **Final tree diagram:**
```text
      A
     / \
    B   C
   / \   \
  D   E   F
```
*   **Algorithm Implementation:**
    ```python
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def build_tree(preorder, inorder):
        if not preorder or not inorder:
            return None
            
        # First element of preorder is the root
        root_val = preorder[0]
        root = Node(root_val)
        
        # Find index of root in inorder array
        root_index = inorder.index(root_val)
        
        # Recursively construct left and right subtrees
        root.left = build_tree(preorder[1:1+root_index], inorder[:root_index])
        root.right = build_tree(preorder[1+root_index:], inorder[root_index+1:])
        
        return root
    ```

**Q7. Complexity Analysis**
*   **(a)** Loop runs from 0 to n-1 (incrementing by 1). 
    *   Time Complexity: $O(n)$. 
    *   Classification: Best = $O(n)$, Average = $O(n)$, Worst = $O(n)$.
*   **(b)** `i` starts at 1 and is multiplied by 3 each iteration. Number of steps $k$ is given by $3^k = n$.
    *   Time Complexity: $O(\log_3 n)$ or simply $O(\log n)$.
    *   Classification: Best = $O(\log n)$, Average = $O(\log n)$, Worst = $O(\log n)$.
*   **(c)** Two nested loops, both running from 0 to n-1. 
    *   Time Complexity: $O(n \times n) = O(n^2)$.
    *   Classification: Best = $O(n^2)$, Average = $O(n^2)$, Worst = $O(n^2)$.

**Q8. Searching Techniques**
**Differentiate between Linear Search and Binary Search:**
*   **Working Principle:** Linear Search checks every element sequentially until a match is found. Binary Search repeatedly divides the sorted search space in half.
*   **Time Complexity:** Linear Search is $O(n)$. Binary Search is $O(\log n)$.
*   **Requirement of Sorting:** Linear Search works on unsorted arrays. Binary Search *requires* the array to be sorted.
*   **Best Use Case:** Linear Search for small or unsorted data. Binary Search for large, sorted datasets.

**Search element 25 in sorted array: `[5, 10, 15, 20, 25, 30, 35]` using Binary Search.**
*   **Initial state:** `low = 0` (value 5), `high = 6` (value 35). Target = 25.
*   **Step 1:** 
    *   `mid = (low + high) // 2 = (0 + 6) // 2 = 3`. 
    *   Array[`mid`] = Array[3] = 20.
    *   Since 25 > 20, we ignore the left half. Update `low = mid + 1 = 4`.
*   **Step 2:**
    *   `low = 4` (value 25), `high = 6` (value 35).
    *   `mid = (4 + 6) // 2 = 5`.
    *   Array[`mid`] = Array[5] = 30.
    *   Since 25 < 30, we ignore the right half. Update `high = mid - 1 = 4`.
*   **Step 3:**
    *   `low = 4` (value 25), `high = 4` (value 25).
    *   `mid = (4 + 4) // 2 = 4`.
    *   Array[`mid`] = Array[4] = 25.
    *   Since 25 == 25, **element is found at index 4**.
*   **Algorithm Implementation:**
    ```python
    def linear_search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
        
    def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    ```
