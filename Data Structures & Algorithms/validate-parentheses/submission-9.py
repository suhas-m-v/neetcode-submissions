class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            else:
                if st and (st[-1]=='(' and ch == ')' or st[-1] == '{' and ch == '}' or st[-1] == '[' and ch == ']'):
                    st.pop()
                else:
                    return False
        if len(st) == 0:
            return True
        return False
                