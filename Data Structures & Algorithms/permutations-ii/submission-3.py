class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        def rand(ind,nums):
            if ind == len(nums):
                ans.append(nums[:])
                return
            seen=set()
            for i in range(ind,len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                
                nums[i],nums[ind]=nums[ind],nums[i]
                rand(ind+1,nums)
                nums[i],nums[ind]=nums[ind],nums[i]
            
        rand(0,nums)
        return ans