class MinStack:
    def __init__(self):
        self.min_value = 0
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_value = val
        else:
            self.min_value = min(val, self.min_value)
        print('min', self.min_value)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        # return self.min_value
        min_val = self.stack[0]
        for val in self.stack:
            min_val = min(val, min_val)
        return min_val
