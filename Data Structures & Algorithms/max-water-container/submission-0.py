class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_value = float("-inf")
        l , r = 0 , len(heights) - 1

        while l < r:
            d = r - l 
            h = min(heights[l],heights[r])
            a = d * h
            max_value = max(a,max_value)
            if heights[l] < heights[r]:
                l += 1 
            else:
                r -= 1
        
        return max_value