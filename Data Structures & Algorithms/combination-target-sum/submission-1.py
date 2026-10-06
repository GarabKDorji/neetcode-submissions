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
            
            path.append(nums[index])
            dfs(index, currSum+nums[index])

            path.pop()
            dfs(index+1, currSum)
        
        dfs(0,0)
        return res