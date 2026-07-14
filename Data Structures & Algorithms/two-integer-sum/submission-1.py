class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen =  {} 
        # nums[j] =  target - nums[i]

        for i,v in enumerate(nums):
            value = target - v 
            if value in seen:
                return [seen[value],i]
            seen[v] = i
        
        return []