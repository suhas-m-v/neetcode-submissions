class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            if ast>=0:
                st.append(ast)
            else: 
                
                while st and st[-1]>0 and st[-1] < abs(ast):
                    st.pop()
                if st and st[-1] == abs(ast):
                    st.pop()
                elif not st or st[-1]<0:
                    st.append(ast)
        return st
                    
                
                

