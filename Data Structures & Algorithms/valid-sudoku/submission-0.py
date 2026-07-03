class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        i = 0 
        while i < len(board):
            seen = set() 
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue 
                if int(board[i][j])  < 0 and int(board[i][j])   > 9:
                    return False
                if board[i][j] not in seen:
                    seen.add(board[i][j] )
                else:
                    return False 
            seen = set()
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue 
                if int(board[j][i])  < 0 and int(board[j][i])  > 9:
                    return False
                if board[j][i] not in seen:
                    seen.add(board[j][i])
                else:
                    return False 
            
            i += 1 
        
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                seen = set()
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] not in seen:
                            seen.add(board[r][c])
                        else:
                            return False 

        return True