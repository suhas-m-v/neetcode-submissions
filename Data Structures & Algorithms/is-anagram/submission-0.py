class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap={}
        tmap={}
        for i in s:
            if i not in smap:
                smap[i]=1
            else:
                smap[i]+=1
        for i in t:
            if i not in tmap:
                tmap[i]=1
            else:
                tmap[i]+=1
        return smap == tmap
        