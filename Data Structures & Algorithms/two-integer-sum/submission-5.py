class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hmap and i != hmap[diff]:
                return [i,hmap[diff]]