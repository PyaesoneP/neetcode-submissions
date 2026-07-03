import math
class MinStack:

    def __init__(self):
        self.items = []
        self.minstack = []
        self.minimum = math.inf

    def push(self, val: int) -> None:
        self.items.append(val)
        if val <= self.minimum:
            self.minimum = val
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.items.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()
            if self.minstack:
                self.minimum = self.minstack[-1]
            else:
                self.minimum = math.inf

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
