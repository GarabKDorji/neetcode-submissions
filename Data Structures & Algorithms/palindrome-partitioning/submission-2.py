class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []

        def isPalindrome(s,l,r):
            
            while l < r:
                if s[l] != s[r]:
                    return False 
                l += 1 
                r -= 1
            
            return True

        def dfs(index): 
            if index >= len(s):
                res.append(part[:])
            
            for i in range(index,len(s)):
                if isPalindrome(s,index,i):
                    part.append(s[index:i+1])
                    dfs(i+1)
                    part.pop()
        
        dfs(0)
        return res