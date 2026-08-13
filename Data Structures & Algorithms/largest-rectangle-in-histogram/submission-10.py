class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        max_area = 0
        for i in range(len(heights)): 
            start = i 
            while stack and stack[-1][1] > heights[i]: 
                index , height = stack.pop()
                area = (i - index) * height
                max_area = max(area, max_area)
                start = index
            stack.append((start,heights[i]))
        
        for i , h in stack: 
            area = (len(heights) - i )*h
            max_area = max(area,max_area)
        
        return max_area