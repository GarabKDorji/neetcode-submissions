class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []

        def dfs(open_num, close_num):

            if open_num == close_num == n:
                res.append("".join(stack))
                return 
            
            if open_num < n:
                stack.append("(")
                dfs(open_num+1, close_num)
                stack.pop()

            if close_num < open_num:
                stack.append(")")
                dfs(open_num, close_num+1)
                stack.pop()

        dfs(0,0)
        return res