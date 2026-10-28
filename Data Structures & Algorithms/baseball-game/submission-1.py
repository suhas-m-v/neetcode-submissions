class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        
        for ch in operations:
            if ch == "+":
                ele=record[-1]+record[-2]
                record.append(ele)
            elif ch == "C":
                record.pop()
            elif ch == "D":
                ele=2 * record[-1]
                record.append(ele)
                
            else:
                record.append(int(ch))
        return sum(record)