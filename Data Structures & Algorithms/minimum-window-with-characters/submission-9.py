class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        freq_t = Counter(t)
        window = defaultdict(int)
        res = [-1,-1]
        shortest = float("inf")
        l = 0 
        have = 0 
        need = len(freq_t)
        for r in range(len(s)):
            char = s[r] 
            window[char] += 1 
            
            if char in freq_t and freq_t[char] == window[char]:
                have += 1 
            
            while have == need: 
                if shortest > r - l + 1:
                    shortest = r - l + 1 
                    res = [l , r]
                
                window[s[l]] -=1 
                if s[l] in freq_t and freq_t[s[l]] > window[s[l]]:
                    have -= 1 
                l += 1 
        
        l , r = res 
        return s[l : r+1]

            