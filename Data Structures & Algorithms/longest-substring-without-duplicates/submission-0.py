class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        freq = {} 
        l = 0 
        res = 0 

        for r in range(len(s)):
            if s[r] in freq:
                l = max(l,freq[s[r]]+1)
            freq[s[r]] = r 
            res = max(r - l + 1 ,res)
    
        return res
            
