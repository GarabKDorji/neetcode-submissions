# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        if subRoot is None:
            return True 
        
        if root is None:
            return False 
        
        if self.compare(root,subRoot):
            return True 
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def compare(self, root, subroot): 
        if not subroot and not root:
            return True 

        if not subroot or not root or root.val != subroot.val : 
            return False 

        return self.compare(root.left, subroot.left) and self.compare(root.right, subroot.right)
        




