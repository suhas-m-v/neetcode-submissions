class FreqStack:

    def __init__(self):
        self.freq={}
        self.group={}
        self.maxfreq=0

    def push(self, val: int) -> None:
        f=self.freq.get(val,0)+1
        self.freq[val]=f

        if f > self.maxfreq:
            self.maxfreq=f
        
        if f not in self.group:
            self.group[f]=[]
        self.group[f].append(val)
        

    def pop(self) -> int:

        ele=self.group[self.maxfreq].pop()
        self.freq[ele]-=1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
            
        return ele

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()