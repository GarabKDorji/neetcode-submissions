class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations = {"+","-","*","/"}
        stack = [] 
        
        for token in tokens:    
            if token in operations: 
                val_1 = stack.pop()
                val_2 = stack.pop()
                if token == "+":
                    s = val_1 + val_2
                elif token == "-":
                    s = val_2 - val_1 

                elif token == "*":
                    s = val_1 * val_2 
                else: 
                    s = int(val_2 / val_1) 
                stack.append(s)
            else:
                stack.append(int(token))
        
        return stack[0]