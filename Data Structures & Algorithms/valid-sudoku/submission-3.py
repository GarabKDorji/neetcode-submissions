class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        i = 0 
        while i < len(board):
            seen = set() 
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue 

                if board[i][j] not in seen:
                    seen.add(board[i][j] )
                else:
                    return False 
            seen = set()
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue 

                if board[j][i] not in seen:
                    seen.add(board[j][i])
                else:
                    return False 
            
            i += 1 
        
        for square in range(len(board)):
            seen = set()
            for i in range(3):
                for j in range(3):
                    box_row = square // 3 
                    box_col = square % 3
                    row = box_row * 3 + i 
                    col = box_col * 3 + j 
                    if board[row][col] == ".":
                        continue 
                    if board[row][col] in seen:
                        return False 
                    seen.add(board[row][col])
        
        return True