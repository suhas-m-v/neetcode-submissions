class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        time=[]
        for pair in pairs:
            el=(target-pair[0])/pair[1]
            time.append(el)
        st=[]
        for i in time:
            if st and st[-1]>=i:
                continue
            else:
                st.append(i)
        return len(st)
            
