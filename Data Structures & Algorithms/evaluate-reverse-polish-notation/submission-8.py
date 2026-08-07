class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        opeartions = {"+", "-", "*" , "/"}
        stack = []
        for token in tokens:
            if token in opeartions:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(b+a)
                elif token == "-":
                    stack.append(b-a)
                elif token == "*":
                    stack.append(b*a)
                elif token == "/":
                    stack.append(int(b/a))

            else:
                stack.append(int(token))

        return stack[0]