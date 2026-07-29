class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 

        freq_s1 = Counter(s1)
        freq = defaultdict(int)
        l = 0 
        for r in range(len(s2)):
            freq[s2[r]] += 1 
            while r - l + 1  > len(s1): 
                freq[s2[l]] -= 1
                if freq[s2[l]] == 0:
                    freq.pop(s2[l])
                l += 1 
            if freq == freq_s1:
                return True 



        
        return False