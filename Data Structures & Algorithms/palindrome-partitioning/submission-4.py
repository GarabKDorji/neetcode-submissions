class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = [] 
        path = [] 
        def isPalin(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False 
                l += 1 
                r -= 1 
            return True 

        def dfs(index): 
            if index == len(s):
                res.append(path[:])
                return 
            
            for i in range(index, len(s)):
                if isPalin(index,i):
                    path.append(s[index: i+1])
                    dfs(i + 1)
                    path.pop()
        dfs(0)
        return res
