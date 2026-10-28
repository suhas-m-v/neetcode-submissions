class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge={}
        st=[]
        res=[]
        for i in range(len(nums2)-1,-1,-1):
            while(len(st)!=0 and nums2[i]>=st[-1]):
                st.pop()
            
            if len(st)==0:
                nge[nums2[i]]=-1
            else:
                nge[nums2[i]]=st[-1]
            
            st.append(nums2[i])
        
        for i in nums1:
            res.append(nge[i])
        return res
