class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        cnt = 1
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == prev:
                cnt+=1
            else:
                cnt-=1
                if cnt == 0:
                    prev = nums[i]
                    cnt = 1
        return prev