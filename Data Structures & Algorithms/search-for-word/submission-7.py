class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()
        res = [] 
        ROW = len(board)
        COL = len(board[0])
        def dfs(r,c,index): 
            if index == len(word):
                return True 
            
            if (r < 0 or c < 0 or 
                r >= ROW or c >= COL or (r,c) in path or 
                board[r][c] != word[index] ):
                return False 
            
            path.add((r,c))
            res = (dfs(r+1,c,index+1) or 
                    dfs(r-1,c,index+1) or 
                    dfs(r,c+1,index+1) or 
                    dfs(r,c-1,index+1) )
            path.remove((r,c))

            return res 
        
        for i in range(ROW):
            for j in range(COL):
                if dfs(i,j,0):
                    return True 
        return False
