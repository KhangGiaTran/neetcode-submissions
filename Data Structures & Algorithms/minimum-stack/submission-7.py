class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack_pos = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_stack_pos.append(0)
        elif val <= self.stack[self.min_stack_pos[-1]]:
            self.min_stack_pos.append(len(self.stack))
        else:
            self.min_stack_pos.append(self.min_stack_pos[-1])
        
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack_pos.pop()

    def top(self) -> int:
        return self.stack[-1]     

    def getMin(self) -> int:
        return self.stack[self.min_stack_pos[-1]]
        
