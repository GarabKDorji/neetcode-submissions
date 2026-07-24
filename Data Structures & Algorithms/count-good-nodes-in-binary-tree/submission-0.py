# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
            res = 0
            def dfs(seen,root):
                non local res
                if not root: 
                    return  
                if seen < root.val:
                    seen = root.val 
                    res += 1 
                dfs(seen, root.left) 
                dfs(seen,root.right)


        '''
        res = 0 
        def dfs(seen,root):
            nonlocal res
            if not root:
                return 
            
            if root.val >= seen: 
                res += 1
                seen = root.val 
            
            dfs(seen, root.left)
            dfs(seen,root.right)
        
        dfs(float("-inf"),root)
        return res