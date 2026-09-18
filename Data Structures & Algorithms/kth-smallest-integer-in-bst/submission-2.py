# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        res = 0
        def smallest(root,k): 
            nonlocal i , res

            if not root:
                return 
            
            smallest(root.left,k)
            i += 1
            if i == k: 
                res = root.val
            
            smallest(root.right,k)

        smallest(root,k)  
        return res           
            
