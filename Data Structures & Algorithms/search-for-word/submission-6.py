class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        part = set()
        def dfs(r,c,index):
            if index == len(word): 
                return True 
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in part or board[r][c] != word[index]):
                return False 
            
            part.add((r,c))
            res = (dfs(r-1,c,index + 1) or 
                    dfs(r+1,c,index +1 ) or
                    dfs(r,c-1,index +1 ) or
                    dfs(r,c+1,index+ 1) )
            part.remove((r,c))

            return res 
    
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True 

        return False
