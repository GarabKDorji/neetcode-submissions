class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(index,currSum): 
            if index >= len(nums) or currSum > target:
                return 
            
            if currSum == target:
                res.append(path[:])
                return

            for i in range(index,len(nums)): 
                path.append(nums[i])
                dfs(i,currSum+nums[i])
                path.pop()
        
        dfs(0,0)
        return res