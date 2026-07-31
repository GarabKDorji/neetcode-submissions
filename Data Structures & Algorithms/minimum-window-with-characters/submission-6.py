class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        freq_t = Counter(t)
        have , need = 0 , len(freq_t)
        res_len = float("inf")
        l = 0
        count = defaultdict(int)
        res = [-1,-1]
        for r in range(len(s)):
            count[s[r]] += 1 
            
            if s[r] in freq_t and count[s[r]] == freq_t[s[r]]:
                have += 1 
            
            while have == need: 
                if r - l + 1 < res_len: 
                    res_len = r - l + 1 
                    res = [l,r]
                count[s[l]] -=1 

                if s[l] in freq_t and freq_t[s[l]] > count[s[l]]:
                    have -= 1 
                
                l += 1 
        
        l,r = res 

        return s[l:r+1]


            