# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0 
        
        left = self.height(root.left)
        right = self.height(root.right)
        diameter = left + right 
        print(diameter)
        v1 = self.diameterOfBinaryTree(root.left)
        v2 = self.diameterOfBinaryTree(root.right)

        return max(diameter,v1,v2)
    
    def height(self, root):
        if not root: 
            return 0 

        if not root.left and not root.right: 
            return 1 
        
        return 1 + max(self.height(root.left),self.height(root.right))