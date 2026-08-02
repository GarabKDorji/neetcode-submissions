class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        window = deque()
        res = [] 
        l = 0
        for r in range(len(nums)):
            while window and nums[window[-1]] < nums[r]:
                window.pop()

            window.append(r)

            if window[0] < l:
                window.popleft()
            
            if r - l +  1 >= k: 
                res.append(nums[window[0]])
                l += 1 
        
        return res

