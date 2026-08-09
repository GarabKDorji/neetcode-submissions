class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0 
        stack = []
        for i in range(len(heights)):
            start = i 
            while stack and stack[-1][1] > heights[i]:
                start, height = stack.pop()
                area =  (i - start) * height 
                max_area = max(area,max_area)
            stack.append((start,heights[i]))

        for i , h in stack:               
            area =  (len(heights) - i) * h
            max_area = max(area,max_area)

        
        return max_area
