class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return False

        map = {"}":"{", "]":"[", ")":"(" }
        stack = [] 

        for i in s: 
            if i in map: 
                if not stack:
                    return False 
                open = stack.pop()
                if open != map[i]:
                    return False 
            else:
                stack.append(i)
        
        return len(stack) == 0
             
