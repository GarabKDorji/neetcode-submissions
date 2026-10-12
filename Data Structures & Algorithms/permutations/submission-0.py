class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        used = [False] * len(nums)
        def dfs(index):
            if len(nums) == len(path):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True 

                dfs(index+1)

                path.pop()
                used[i] = False 
        
        dfs(0)
        return res
 