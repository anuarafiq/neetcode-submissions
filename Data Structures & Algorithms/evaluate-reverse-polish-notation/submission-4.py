class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                x = stack.pop()
                y = stack.pop()                
                val = eval(f"{y}{t}{x}")
                stack.append(int(val))
            else: stack.append(int(t))

        return int(stack[-1])