class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[i] == val and nums[j]!=val:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            if nums[i]!=val:
                i+=1
        return i