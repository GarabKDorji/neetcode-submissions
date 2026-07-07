class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        count_t = Counter(t)
        res = ""
        res_len = float("inf")
        window = {} 
        have, need = 0, len(count_t)
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char,0) + 1 

            if char in count_t and count_t[char] == window[char]:
                have += 1
            
            while have == need: 
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]
                
                window[s[l]] -=1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1 
                l += 1 

        return res 


            