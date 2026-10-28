class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        def subs(ind,ds):
            ans.append(ds[:])       
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue
                
                ds.append(nums[i])
                subs(i+1,ds)
                ds.pop()
        subs(0,[])
        return ans
