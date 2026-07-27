class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        l = 0 
        seen = dict()
        longest = 0

        for r in range(len(s)):

            if s[r] in seen: 
                l = max(seen.get(s[r],0) + 1,l) 
            
            seen[s[r]] = r 
            longest = max(longest, r - l + 1)
      
        return longest
