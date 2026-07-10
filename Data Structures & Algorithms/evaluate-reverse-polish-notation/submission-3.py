class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [] 
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            
            if token not in operators:
                stack.append(int(token))
            else:
                right = int(stack.pop())
                left = int(stack.pop())

                if token == "+":
                    value = left + right
                elif token == "-":
                    value = left - right 
                elif token == "*":
                    value = left * right 
                elif token == "/":
                    value = int(left / right )
                
                stack.append(value)
        
        return stack[0]