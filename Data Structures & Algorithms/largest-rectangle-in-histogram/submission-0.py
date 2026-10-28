class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        def findnse():
            st=[]
            nse=[n]*n
            for i in range(n-1,-1,-1):
                while st and heights[st[-1]]>=heights[i]:
                    st.pop()
                
                if st:
                    nse[i]=st[-1]
                st.append(i)
            return nse
        def findpse():
            st=[]
            pse=[-1]*n
            for i in range(n):
                while st and heights[st[-1]]>heights[i]:
                    st.pop()
                
                if st:
                    pse[i]=st[-1]
                st.append(i)
            return pse
        max_area=0
        nse=findnse()
        pse=findpse()
        for i in range(n):
            max_area=max(max_area,heights[i]*(nse[i]-pse[i]-1))
        return max_area



