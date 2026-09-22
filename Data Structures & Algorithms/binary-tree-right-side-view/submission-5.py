# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque([root])
        res = []
        if not root:
            return res
        
        while q: 
            l = len(q)
            right_side = None
            for _ in range(l):

                node = q.popleft()
                right_side = node 
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            res.append(right_side.val)
        
        return res

