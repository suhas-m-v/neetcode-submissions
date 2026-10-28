class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = sorted(strs)
        start = temp[0]
        last = temp[len(strs)-1]
        ans = ""
        for i in range(len(start)):
            if start[i] == last[i]:
                ans+=start[i]
            else:
                break

        return ans