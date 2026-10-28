class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def combs(ind,ds,target):
            if target == 0:
                ans.append(ds[:])
                return
            if ind == len(candidates) or target < 0:
                return
            for i in range(ind,len(candidates)):
                if i > ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                combs(i+1,ds,target-candidates[i])
                ds.pop()
        combs(0,[],target)
        return ans