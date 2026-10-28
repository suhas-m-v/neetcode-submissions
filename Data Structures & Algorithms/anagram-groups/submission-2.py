from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def freq(word):
            key = [0]*26
            for let in word:
                key[ord(let)-97]+=1
            return tuple(key)
        grops = defaultdict(list)
        for word in strs:
            key = freq(word)
            grops[key].append(word)
        return list(grops.values())











