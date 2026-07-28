# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:  
        
        if not root:
                return float("-inf")

        # Best downward paths from the left and right children
        left = self.getMax(root.left)
        right = self.getMax(root.right)

        # Best path whose highest point is the current node
        through_root = root.val + left + right

        # Best path completely inside the left subtree
        left_res = self.maxPathSum(root.left)

        # Best path completely inside the right subtree
        right_res = self.maxPathSum(root.right)

        return max(through_root, left_res, right_res) 


    def getMax(self, root):
        if not root:
            return 0 
        
        left = self.getMax(root.left)
        right = self.getMax(root.right)
        value = root.val  + max(left,right)
        return max(0,value)
    