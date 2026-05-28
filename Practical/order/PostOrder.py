class Solution:
    def postorderTraversal(self, root):
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            print(node.val, end=" ")   # print
        
        dfs(root)