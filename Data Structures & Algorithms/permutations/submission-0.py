class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def rand(ind,nums):
            if ind ==  len(nums):
                ans.append(nums[:])
                return
            
            for i in range(ind,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                rand(ind+1,nums)
                nums[ind],nums[i]=nums[i],nums[ind]
        rand(0,nums)
        return ans