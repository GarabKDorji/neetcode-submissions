class Solution:
    def isValid(self, s: str) -> bool:

        
        map = { "}" : "{", "]": "[", ")":"("}
        stack = [] 
        for i in s:
            if i in map: 
                if not stack:
                    return False
                elif stack[-1] != map[i]:
                    return False 
                else:
                    stack.pop()
            else:
                stack.append(i)

        
        return len(stack) == 0
            
            




        