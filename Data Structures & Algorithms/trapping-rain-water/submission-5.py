class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        res = 0 
        left_max= []
        right_max = [0] * len(height)
        max_left = 0
        for i in range(len(height)):
            max_left = max(max_left,height[i])
            left_max.append(max_left)
        
        max_right = 0
        for i in range(len(height)-1,-1,-1):
            max_right = max(max_right,height[i])
            right_max[i] = max_right
        
        for i in range(len(height)):
            res += min(left_max[i],right_max[i]) - height[i]
        
        return res
