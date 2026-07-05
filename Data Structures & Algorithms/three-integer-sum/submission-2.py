class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [] 

        nums.sort()
        res = [] 
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue

            l ,r = i+1 , len(nums)-1 
            while l < r:
                s = a + nums[l] + nums[r]
                if s > 0:
                    r -= 1 
                elif s < 0:
                    l += 1 
                else:
                    res.append([a,nums[l],nums[r]])

                    #[-2,-2,0,0,2,2]
                    l += 1 
                    while l < r and  nums[l] == nums[l-1]:
                        l += 1 
                    r -=1 
                    while l< r and nums[r] == nums[r+1]:
                        r -=1 
        return res