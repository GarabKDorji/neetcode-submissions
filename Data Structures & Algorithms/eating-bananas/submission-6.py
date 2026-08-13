class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_hour = float('inf')
        max_value = max(piles)
        value = 0
        l = 1 
        r = max(piles)

        while l <= r:
            mid = (l +r)//2 
            hours = 0
            for p in piles: 
                hours += (p + mid - 1) // mid 

            if hours > h: 
                l = mid + 1 
            else: 
                r = mid - 1 
                res = mid 
        
        return res


         