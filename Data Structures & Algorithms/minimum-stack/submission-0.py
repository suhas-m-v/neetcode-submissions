class MinStack:

    def __init__(self):
        self.s1=[]

    def push(self, val: int) -> None:
        if len(self.s1)==0:
            self.s1.append((val,val))
        else:
            tm=self.s1[-1][-1]
            self.s1.append((val,min(tm,val)))

    def pop(self) -> None:
        self.s1.pop()

    def top(self) -> int:
        return self.s1[-1][0]

    def getMin(self) -> int:
        return self.s1[-1][-1]
        
