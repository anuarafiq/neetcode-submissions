class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in {')', ']', '}'}:
                if stack and c == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                if c == '(': stack.append(')')
                elif c == '[': stack.append(']')
                else: stack.append('}')

        return len(stack) == 0