class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            len(window) - max_freq  =characters that can be replaced
        '''
        longest = 0 

        for i in range(len(s)):
            freq = defaultdict(int)
            max_freq = 0 
            for j in range(i,len(s)):
                freq[s[j]] += 1
                max_freq = max(freq[s[j]],max_freq)

                if (j - i + 1) - max_freq > k:
                    break 
                longest = max(longest,j - i + 1 )
        
        
        return longest


