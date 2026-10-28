class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        top=-1
        for ch in operations:
            if ch == "+":
                ele=record[top]+record[top-1]
                record.append(ele)
                top+=1
            elif ch == "C":
                record.pop()
                top-=1
            elif ch == "D":
                ele=2 * record[top]
                record.append(ele)
                top+=1
            else:
                record.append(int(ch))
                top+=1
        return sum(record)