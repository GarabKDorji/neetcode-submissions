class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
                

        longest = 0

        for i in range(len(s)):
            count = 0
            freq = defaultdict(int) 
            max_freq = 0
            for j in range(i,len(s)):
                freq[s[j]] += 1
                max_freq = max(max_freq,freq[s[j]])
                if (j-i+1) - max_freq > k:
                    break
                longest = max(longest,j-i+1)
     
        
        return longest