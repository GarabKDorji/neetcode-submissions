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
        left_max = []
        right_max = []
        
        left = 0
        for i in range(len(height)):
            left = max(left,height[i])
            left_max.append(left)
        
        right = 0
        for i in range(len(height)-1, -1 ,-1):
            right = max(right,height[i])
            right_max.append(right)
        right_max.reverse()

        res = 0 
        for i in range(len(height)):
            res += min(left_max[i],right_max[i]) - height[i]
        
        return res 
        
        
        
        
