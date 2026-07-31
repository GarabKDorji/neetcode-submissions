class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        freq1 = Counter(s1)
        for i in range(len(s2)- len(s1)+1): 
            sub = Counter(s2[i:i+len(s1)])
            print(sub)
            if sub == freq1:
                return True 
        
        return False

