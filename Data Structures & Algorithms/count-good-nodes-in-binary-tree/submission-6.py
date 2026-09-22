# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
         
        
        count = 0 
        def dfs(root,max_value): 
            nonlocal count

            if not root:
                return 

            if max_value <= root.val:
                count += 1 
            max_value = max(max_value, root.val) 
            
            dfs(root.left,max_value)
            dfs(root.right, max_value)
        
        dfs(root,float("-inf"))
        return count
            
            