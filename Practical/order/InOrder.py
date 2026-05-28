class Solution:
    def inorderTraversal(self, root):
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            print(node.val, end=" ")   # Root in middle
            dfs(node.right)
        
        dfs(root)