class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if not t.isdigit():
                val = eval(f"{stack.pop()} {t} {stack.pop()}")
                stack.append(val)
            else: stack.append(t)

        return stack[-1]