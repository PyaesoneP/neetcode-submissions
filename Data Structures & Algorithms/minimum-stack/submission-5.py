class MinStack:

    def __init__(self):
        self.items = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.items.append(val)

        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.items.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
