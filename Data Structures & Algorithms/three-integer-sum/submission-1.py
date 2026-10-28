class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def twop(target,l,r):
            while l<r:
                temp = nums[l]+nums[r]
                if target == temp:
                    ans.append([-target,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif temp < target:
                    l+=1
                elif temp > target:
                    r-=1
        
        j = len(nums)-1
        for i in range(len(nums)-2):
            if i >0 and nums[i]==nums[i-1]:
                continue
            tar = -nums[i]
            twop(tar,i+1,j)
        return ans