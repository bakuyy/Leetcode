import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for i in tokens:
            if i in operators:
                first = int(stack[-2])
                second = int(stack[-1])
                if i == "+":
                    stack.append(int(first+second))
                elif i == "-":
                    stack.append(int(first-second))
                elif i == "*":
                    stack.append(int(first*second))
                elif i == "/":
                    stack.append(int(first/second))
                for i in range(2):
                    stack.pop(-2)
            else:
                stack.append(int(i))
        return stack[0]