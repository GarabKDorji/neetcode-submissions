class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_pile = max(piles)

        l = 1 
        r = max_pile 
        res = 0

        while l <= r:
            mid = (l + r)//2 
            hour = 0

            for pile in piles: 
                hour += math.ceil(pile/mid)
            
            if hour <= h:
                r = mid - 1 
                res = mid
            else:
                l = mid + 1 

        
        return res


            
            