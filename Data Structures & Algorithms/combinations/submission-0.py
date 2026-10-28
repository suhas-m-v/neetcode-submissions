class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[]
        ans=[]
        for i in range(1,n+1):
            nums.append(i)
        def subs(ind,ds):
            if ind == n and len(ds) == k:
                ans.append(ds[:])
                return
            if ind == n:
                return
            ds.append(nums[ind])
            subs(ind+1,ds)
            ds.pop()
            subs(ind+1,ds)
        subs(0,[])
        return ans