class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq_t = Counter(t)
        res = [-1,-1]
        shortest = float("inf")
        for i in range(len(s)):
            freq_s = defaultdict(int)
            for j in range(i,len(s)):
                freq_s[s[j]] += 1 
                
                found = True 
                for k in freq_t: 
                    if freq_s[k] < freq_t[k]:
                        found = False 
                        break 

                if found and shortest > j - i + 1 :
                    res = [i,j]
                    shortest = j - i +1
                    break

        l ,r = res 
        return s[l :r+1]