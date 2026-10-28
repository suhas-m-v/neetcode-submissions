class MyQueue:

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        s2=[]
        for i in range(len(self.stack)-1,-1,-1):   
            s2.append(self.stack[i])
            del self.stack[i]
        el=s2.pop()
        for i in range(len(s2)-1,-1,-1):
            self.stack.append(s2[i])
        return el


    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()