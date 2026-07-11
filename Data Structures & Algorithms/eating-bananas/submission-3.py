class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_value = max(piles)
        r = max_value
        l = 1
        while l <= r:
            mid = (l+r)//2 
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid)
            
            if total_hours <= h:
                r = mid - 1 
            else:
                l = mid +1 
        
        return l
            


