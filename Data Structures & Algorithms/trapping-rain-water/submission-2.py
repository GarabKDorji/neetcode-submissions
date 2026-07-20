class Solution:
    def trap(self, height: List[int]) -> int:
    
        if not height:
            return 0 
        
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left = 0
        for i in range(len(height)):
            left = max(left, height[i])
            left_max[i] = left  
        
        right = 0 
        for i in range(len(height)-1,-1,-1):
            right = max(right,height[i])
            right_max[i] = right 
        
        res = 0 
        for i in range(len(height)):
            res += min(left_max[i],right_max[i]) - height[i]
        
        return res