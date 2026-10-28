class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxl,maxr=0,0
        water=0
        l,r=0,n-1
        while l<r:
            if height[l]<height[r]:
                maxl=max(maxl,height[l])
                water+=maxl-height[l]
                l+=1
            else:
                maxr=max(maxr,height[r])
                water+=maxr-height[r]
                r-=1
        return water