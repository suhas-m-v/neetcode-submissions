class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.st.append((val,val))
        else:
            prev_min = self.st[-1][-1]
            self.st.append((val,min(prev_min,val)))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return  self.st[-1][-1]
        
