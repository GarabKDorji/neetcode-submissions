class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def dfs(index,currSum): 
            if index >= len(nums) or currSum > target:
                return 
            
            if currSum == target:
                res.append(path[:])
                return

            for i in range(index,len(nums)): 
      
                if currSum+nums[i] > target:
                    break
                path.append(nums[i])   
                dfs(i,currSum+nums[i])
                path.pop()
        
        dfs(0,0)
        return res