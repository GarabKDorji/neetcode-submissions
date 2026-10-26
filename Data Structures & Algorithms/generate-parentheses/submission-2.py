class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = [] 
        path = []

        def dfs(open_num, close_num):
            if open_num == close_num == n:
                res.append("".join(path))
            if open_num < n: 
                path.append("(") 
                dfs(open_num+1, close_num)
                path.pop()
            
            if close_num < open_num:
                path.append(")")
                dfs(open_num, close_num+1)
                path.pop()
        
        dfs(0,0)
        return res