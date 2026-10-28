class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        r=x
        while l<=r:
            mid=(l+r)//2
            temp=mid*mid
            if temp<=x:
                ans=mid
                l=mid+1
            elif temp>x:
                r=mid-1
            else:
                l=mid+1
        return l-1