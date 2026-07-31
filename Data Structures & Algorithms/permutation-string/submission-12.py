class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        freq1 = Counter(s1)
        l = 0 
        freq2 = defaultdict(int)
        for r in range(len(s2)):
            freq2[s2[r]] += 1
            if r - l + 1 > len(s1): 
                freq2[s2[l]] -=1 
                if freq2[s2[l]] ==0:
                    freq2.pop(s2[l])
                l += 1 

            if freq1 == freq2:
                return True 
        
        return False


