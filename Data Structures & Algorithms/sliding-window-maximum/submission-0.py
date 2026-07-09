class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if k == 0:
            return nums

        res = [] 
        for i in range(len(nums)-k+1):
            max_value =float("-inf")
            for j in range(i,i+k):
                max_value = max(max_value,nums[j])
            res.append(max_value)
        
        return res
