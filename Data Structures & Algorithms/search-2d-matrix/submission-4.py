class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix) 
        COLUMNS = len(matrix[0])

        l = 0 
        r = ROWS - 1    

        while l <= r: 
            mid = (r + l)//2 
            if matrix[mid][-1] < target: 
                l = mid + 1 
            elif matrix[mid][0] > target:
                r = mid - 1 
            else:
                break 
        
        if l > r:
            return False 
        
        row = mid
        l = 0 
        r = COLUMNS - 1 
        while l <= r: 
            mid = (r + l)//2 
            if matrix[row][mid] < target:
                l = mid + 1 
            elif matrix[row][mid] > target:
                r = mid - 1 
            else:
                return True 
        
        return False 