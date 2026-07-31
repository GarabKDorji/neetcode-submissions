class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        freq_t = Counter(t)
        res_len = float("inf")
        res = [-1,-1]
        for i in range(len(s)): 
            count = defaultdict(int)
            for j in range(i, len(s)): 
                count[s[j]] += 1 

                found = True 
                for c in freq_t: 
                    if count[c] < freq_t[c]:
                        found = False 
                        break 
                    
                if found and j - i + 1 < res_len: 
                    res_len = j - i + 1
                    res = [i,j]
        
        return s[res[0]:res[1] + 1]
                


