class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix) 
        COLS = len(matrix[0])

        l = 0 
        r = ROWS - 1 
        while l <= r: 
            mid = (l + r)//2 
            if matrix[mid][-1] <  target: 
                l = mid + 1 
            elif matrix[mid][0] > target: 
                r = mid - 1 
            else:
                break 
            
        if l > r :
            return False 
        
        row = mid 

        l = 0 
        r = COLS - 1 
        while l <=r : 
            mid =( l +r ) //2 
            if matrix[row][mid] == target:
                return True 
            elif matrix[row][mid] <  target: 
                l = mid + 1 
            else: 
                r = mid - 1 
        
        return False