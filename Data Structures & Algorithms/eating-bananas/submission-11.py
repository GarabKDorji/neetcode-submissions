class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_hour = max(piles)
        l = 1
        r = max_hour
        res = -1
        while l <= r :
            mid = (l + r) // 2  
            hour = 0 
            for pile in piles: 
                hour += math.ceil(pile/mid)
            
            if hour > h :
                l  = mid + 1
            else:
                r = mid - 1 
                res = mid 

                
            
        return res