class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=[]
        def subset(ind,ds):
            if ind == len(nums):
                ans.append(ds[:])
                return
            
            ds.append(nums[ind])
            subset(ind+1,ds)
            ds.pop()
            subset(ind+1,ds)
        subset(0,[])
        tot=0
        for arr in ans:
            if arr:
                xsum=0
                for i in arr:
                    xsum^=i
                tot+=xsum
        return tot

