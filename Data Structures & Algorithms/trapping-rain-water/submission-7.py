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
        for i in range(len(height)):
            left_max = height[i]
            right_max = height[i]

            for j in range(i):
                left_max = max(left_max,height[j])

            for j in range(i+1, len(height)):
                right_max = max(right_max,height[j])
            
            res += min(right_max,left_max) - height[i]
        return res 
