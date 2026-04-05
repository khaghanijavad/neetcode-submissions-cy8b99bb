class MinStack:

    def __init__(self):
        self.values = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.values.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        self.minstack.append(val)

        

    def pop(self) -> None:
        self.values.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.values[-1]

        

    def getMin(self) -> int:
        return self.minstack[-1]
