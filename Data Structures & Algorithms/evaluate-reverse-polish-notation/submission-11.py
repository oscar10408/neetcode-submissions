class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+','-','*','/'}

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            
            elif token == '+':
                stack.append(stack.pop() + stack.pop())
            
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif token == '*':
                stack.append(stack.pop() * stack.pop())

            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
        
        return stack[-1]