class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        need = Counter(t)
        res = ""
        res_len = float("inf")
        for i in range(len(s)):
            count = defaultdict(int)
            for j in range(i,len(s)):
                count[s[j]] += 1 

                flag = True 
                for key in need:
                    if count[key] < need[key]:
                        flag = False 
                        break 
                
                if flag:
                    if (j-i+1) < res_len:
                        res_len = j-i+1 
                        res = s[i:j+1]
                        break 
        return res 