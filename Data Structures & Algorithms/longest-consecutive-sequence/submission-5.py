class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for num in nums:
            if (num - 1) not in nums_set:
                length = 0 
                curr = num 
                while curr in nums_set:
                    curr += 1 
                    length += 1 
                longest = max(longest, length)
        
        return longest