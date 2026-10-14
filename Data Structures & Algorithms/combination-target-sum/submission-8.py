class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []

        def dfs(currSum, index): 
            if currSum == target:
                res.append(path[:])
                return 
            
            if currSum > target or index >= len(nums):
                return
            
            for i in range(index,len(nums)):
                path.append(nums[i])
                dfs(currSum + nums[i],i)
                path.pop()
            
        dfs(0,0)
        return res