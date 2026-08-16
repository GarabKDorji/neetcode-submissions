class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_value = max(piles)
        res= 0

        l = 1
        r = max_value 

        while l <= r:
            mid = (l+r)//2 
            hour = 0
            for pile in piles: 
                hour +=  math.ceil(pile/mid)
            print(hour, mid)
            if hour >  h: 
                l = mid + 1 
            else : 
                r = mid - 1 
                res = mid 
        
        return res
