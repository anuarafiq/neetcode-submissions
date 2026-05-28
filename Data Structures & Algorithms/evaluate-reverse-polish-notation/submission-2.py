class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if not t.isdigit():
                val = eval(f"{stack[-2]} {t} {stack[-1]}")
                stack.pop()
                stack.pop()
                stack.append(val)
            else: stack.append(t)

        return int(stack[-1])