class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        used = [False] * len(nums)
        res = [] 
        for i in range(len(nums)):
            used[i] = True 
            product = 1
            for j in range(len(nums)):
                if not used[j]:
                    product *= nums[j]
            res.append(product)
            used[i] = False 
        return res