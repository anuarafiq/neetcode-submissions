class MinStack:
    """
    self.stack = [1]
    self.min_stack = []
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.getMin():
            self.min_stack.append(val)

    def pop(self) -> None:
        curr = self.stack.pop()
        if curr == self.getMin() and self.min_stack:
            self.min_stack.pop()

    def top(self) -> int:       
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else 2^31
