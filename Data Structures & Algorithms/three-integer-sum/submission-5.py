class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = [] 
        nums.sort()

        for i in range(len(nums)):

            if i != 0 and nums[i-1] == nums[i]:
                continue 

        
            l = i + 1 
            r = len(nums) - 1 

            while l < r: 
                s = nums[i] + nums[l] + nums[r] 
                if s < 0: 
                    l += 1 
                elif s > 0: 
                    r -= 1 
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l+= 1 
                    r -= 1
                    while l+1 < len(nums) and nums[l-1] == nums[l]:
                        l += 1 
            
            
        return res
            