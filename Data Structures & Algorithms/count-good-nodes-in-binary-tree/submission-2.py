# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(root, max_seen):
            
            if not root:
                return 0 

            if root.val >= max_seen:
                count = 1
                max_seen = max(root.val,max_seen)
            else:
                count = 0

            count += dfs(root.left, max_seen)
            count += dfs(root.right,max_seen)
            return count

        return dfs(root,root.val)
      
            