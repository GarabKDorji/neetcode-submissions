class Solution:
    def isValid(self, s: str) -> bool:

        
        close_to_opening = { "}" : "{", "]": "[", ")":"("}
        stack = [] 
        for i in s:
            if i in close_to_opening : 
                if not stack or stack[-1] != close_to_opening[i] :
                    return False

                stack.pop()
            else:
                stack.append(i)

        
        return len(stack) == 0
            
            




        