class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        window = nums[:k]
        l = 0 
        max_value = max(window)
        res = [max_value]

        for r in range(k,len(nums)): 
            window.append(nums[r])
       
            if r - l + 1 > k: 
                window.pop(0)
                l +=1 
            max_value = max(window)
            res.append(max_value)
        
        return res


