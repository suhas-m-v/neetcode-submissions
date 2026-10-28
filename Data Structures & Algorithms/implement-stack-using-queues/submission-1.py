from collections import deque
class MyStack:

    def __init__(self):
        self.dq=deque([])

    def push(self, x: int) -> None:
        self.dq.append(x)
        for i in range(len(self.dq)-1):
            self.dq.append(self.dq.popleft())

    def pop(self) -> int:
        ele=self.dq.popleft()
        return ele

    def top(self) -> int:
        return self.dq[0]

    def empty(self) -> bool:
        if len(self.dq)==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()