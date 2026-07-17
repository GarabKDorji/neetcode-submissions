class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                    
                if board[i][j] in seen:
                    return False
                
                seen.add(board[i][j])
            
            seen = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                    
                if board[j][i] in seen:
                    return False
                
                seen.add(board[j][i])

        for i in range(len(board)):      
            seen = set()
            for r in range(3):
                for c in range(3):

                    row = i // 3 
                    col = i % 3 
                    box_row = row * 3 + r
                    box_col = col * 3 + c 
                    if board[box_row][box_col] == ".":
                        continue
                    if board[box_row][box_col] in seen:
                        return False 
                    seen.add(board[box_row][box_col])
        
        return True


