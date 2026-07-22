class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0 
        for i in range(len(height)):
            left_max = height[i]
            right_max = height[i]
            for j in range(i):
                left_max = max(left_max,height[j])
            
            for j in range(i+1,len(height)):
                right_max = max(right_max,height[j])
            res += min(right_max,left_max) - height[i]
    
        return res 
        
