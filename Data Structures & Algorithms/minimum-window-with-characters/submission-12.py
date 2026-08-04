class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count_t = Counter(t)
    
        res = [-1,-1]
        min_len = float("inf")
        l = 0
        have = 0 
        need = len(count_t)
        count_s = defaultdict(int)
        for r in range(len(s)):
            count_s[s[r]] += 1  

            if s[r] in count_t and count_t[s[r]] == count_s[s[r]]:
                have += 1 
            
            while have == need: 
                if r - l + 1 < min_len:
                    res = [l,r]
                    min_len = r - l + 1 
                
                count_s[s[l]] -= 1 
                if s[l] in count_t and count_t[s[l]] > count_s[s[l]]:
                    have -= 1 
                l += 1 
                
        
        l , r = res 
        return s[l: r+1]