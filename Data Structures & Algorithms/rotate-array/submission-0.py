class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        rev=nums[::-1]
        temp = rev[:k][::-1]
        
        nums[:] = temp + rev[k:][::-1]
        