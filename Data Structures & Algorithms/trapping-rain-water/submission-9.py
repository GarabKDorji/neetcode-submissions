class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            Input - list 
            output - int returns the max area of water that can be trapped between the bars 
            E/C - if not height return 0 
                    1 <= height.length <= 1000
                    0 <= height[i] <= 100
            this is the key idea - min(left,right) - height[i]
        '''
        if not height:
            return 0
        res = 0 
        left_max = 0
        right_max = 0 
        l = 0 
        r = len(height) - 1 

        while l < r: 
            if height[l] <= height[r]:
                left_max = max(left_max,height[l])
                res += left_max - height[l]
                l += 1 
            else:
                right_max = max(right_max,height[r])
                res += right_max - height[r]
                r -= 1 
        
        return res

        
        
        
        
