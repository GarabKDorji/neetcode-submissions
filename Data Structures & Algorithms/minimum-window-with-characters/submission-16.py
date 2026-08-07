class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        min_len = float("inf")
        count_t = Counter(t)
        have = 0 
        need = len(count_t)
        window = defaultdict(int)
        res = [-1,-1 ]
        l = 0 
        for r in range(len(s)):
            c = s[r]    
            window[c] += 1 

            if c in count_t and count_t[c] == window[c]:
                have += 1 
            
            while have == need: 
                if min_len > r - l + 1:
                    min_len = r - l + 1 
                    res = [l,r]
                
                window[s[l]] -= 1 
                if s[l] in count_t and count_t[s[l]] > window[s[l]]:
                    have -= 1 
                
                l += 1
        
        l ,r = res 
        return s[l: r +1 ]
                
            


