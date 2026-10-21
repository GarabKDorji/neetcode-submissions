class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(open_num, closed_num): 

            if open_num == closed_num == n: 
                res.append("".join(stack))
                return 

            if open_num < n: 
                stack.append("(")
                dfs(open_num+1, closed_num)
                stack.pop()
            
            if closed_num < open_num:
                stack.append(")")
                dfs(open_num, closed_num+1)
                stack.pop()
            
        dfs(0,0)
        return res
            
