class Solution:
    def simplifyPath(self, path: str) -> str:
        files=list(path.split("/"))
        st=[]
        for file in files:
            if file=="" or file==".":
                continue
            elif file=="..":
                if st:
                    st.pop()
            else:
                st.append(file)
        res="/"+"/".join(st)
        return res