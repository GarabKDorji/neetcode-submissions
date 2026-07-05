class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if not numbers:
            return [] 

        l = 0 
        r = len(numbers) - 1 
        while l < r:
            v = numbers[l] + numbers[r]
            if v > target:
                r -= 1 
            elif v < target:
                l += 1 
            else:
                return [l+1,r+1]

        return []
