# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0 
        answer = 0
        def dfs(root):
            nonlocal index, answer 

            if not root:
                return 
            
            dfs(root.left)
            index += 1 
            if index == k:
                answer = root.val 
            dfs(root.right)
        dfs(root)    
        return answer
