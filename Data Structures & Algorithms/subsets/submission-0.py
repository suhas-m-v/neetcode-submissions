class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def sub(ind,ds):
            if ind == len(nums):
                ans.append(ds[:])
                return
            
            ds.append(nums[ind])
            sub(ind+1,ds)
            ds.pop()
            sub(ind+1,ds)
        sub(0,[])
        return ans