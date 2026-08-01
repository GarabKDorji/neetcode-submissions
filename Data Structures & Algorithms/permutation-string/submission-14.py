class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): 
            return False 

        freq1 = Counter(s1)

        for i in range(len(s2)-len(s1)+1): 
            sub = s2[i:i+len(s1)]
            freq_sub = Counter(sub)
            if freq_sub == freq1:
                return True 
        
        return False
