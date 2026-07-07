class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l = 0 
        s1 = Counter(s1)
        window = Counter()

        for r in range(len(s2)):
            window[s2[r]] += 1 

            if r - l + 1 > n:
                window[s2[l]] -= 1 
                if  window[s2[l]] == 0:
                    window.pop(s2[l])
                l += 1 
            if s1 == window:
                return True 
        
        return False

            