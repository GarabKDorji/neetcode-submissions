class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count_t = Counter(t)
    
        res = [-1,-1]
        min_len = float("inf")

        for i in range(len(s)):
            count_s = defaultdict(int)
            for j in range(i,len(s)):
                count_s[s[j]] += 1 

                found = True
                for k in count_t:
                    if count_t[k] > count_s[k]:
                        found = False 
                        break 
            

                if found and  j - i + 1 < min_len:
                    res = [i,j]
                    min_len = j - i + 1 
        
        l , r = res 
        return s[l: r+1]