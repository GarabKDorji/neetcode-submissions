class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        def dfs(index, r, c):

            if index == len(word):
                return True 
            
            if(r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r,c) in path or board[r][c] != word[index]):
                return False 
            path.add((r,c))
            res = (dfs(index+1,r+1, c) or 
                    dfs(index+1,r-1 ,c) or 
                    dfs(index+1,r, c+1) or 
                    dfs(index+1,r, c-1))
            path.remove((r,c))

            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(0, i, j):
                    return True 
        
        return False