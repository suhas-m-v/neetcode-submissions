class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        def combs(ind,ds,target):
            if target == 0:
                ans.append(ds[:])
                return
            if ind == len(nums) or target < 0:
                return
            if nums[ind]<=target:
                ds.append(nums[ind])
                combs(ind,ds,target-nums[ind])
                ds.pop()
                combs(ind+1,ds,target)
        combs(0,[],target)
        return ans