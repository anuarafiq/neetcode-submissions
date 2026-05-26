class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.getMin():
            self.min_stack.append(val)

    def pop(self) -> None:
        curr = self.stack.pop()
        if curr == self.getMin():
            self.min_stack.pop()

    def top(self) -> int:       
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else 2^31 - 1
