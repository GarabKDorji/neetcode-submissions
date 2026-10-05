class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(index, curr_sum):
            if curr_sum > target:
                return 
            
            if curr_sum == target:
                res.append(path[:])
                return 
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i, curr_sum+ nums[i])
                path.pop()

        dfs(0,0)
        return res