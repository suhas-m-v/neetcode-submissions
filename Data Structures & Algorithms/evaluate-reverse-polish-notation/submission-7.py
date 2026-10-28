class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for ch in tokens:
            if  ch=='+':
                c1=st.pop()
                c2=st.pop()
                st.append(c1+c2)
            elif  ch=='-':
                c1=st.pop()
                c2=st.pop()
                st.append(c2-c1)
            elif ch=='*':
                c1=st.pop()
                c2=st.pop()
                st.append(c1*c2)
            elif  ch=='/':
                c1=st.pop()
                c2=st.pop()
                st.append(int(c2/c1))
            else:
                st.append(int(ch))
        return st[-1]