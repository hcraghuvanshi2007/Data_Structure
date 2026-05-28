class Solution:
    def preorderTraversal(self, root):
        
        def dfs(node):
            if not node:
                return
            
            print(node.val, end=" ")   # ✅ ROOT first
            dfs(node.left)             # Left
            dfs(node.right)            # Right
        
        dfs(root)