class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1 

        while l < r: 
            mid = (r + l) //2 
            if nums[mid] > nums[r]:
                l = mid +1 
            else: 
                r = mid 
        
        pivot = l
        if nums[l] <= target <= nums[len(nums) - 1 ]:
            l = pivot 
            r = len(nums) -1 
        else:
            l = 0 
            r = pivot - 1 
        
        while l <= r:
            mid = (r + l) // 2 
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1 
        
        return -1

        
