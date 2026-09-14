# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque([root])
        res = []
   
        while q: 
            l = len(q)
            row = []
            for _ in range(l): 
                node = q.popleft()  
                if node:
                    row.append(node.val)

                    if node.left: 
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)
            if row:
                res.append(row)
        
        return res


            
