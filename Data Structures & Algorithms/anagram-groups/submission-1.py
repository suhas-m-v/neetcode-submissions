from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def anagram(str1,str2):
        #     if len(str1)!=len(str2):
        #         return False
        #     temp1= Counter(str1)
        #     temp2 = Counter(str2)
        #     if temp1 == temp2:
        #         return True
        #     return False
        # ans = []  
        # seen = set()
        # hset = set(strs)
        # for i in range(len(strs)):
        #     if strs[i] in seen:
        #         continue
        #     temp = []
        #     temp.append(strs[i])
        #     seen.add(strs[i])
        #     for j in range(len(strs)):
                
        #         if i == j:
        #             continue
        #         if anagram(strs[i],strs[j]):
        #             temp.append(strs[j])
        #             seen.add(strs[j])
        #     ans.append(temp)
        # return ans

        hmap = defaultdict(list)
        for i in range(len(strs)):
            word =strs[i]
            word = ''.join(sorted(word))
            hmap[word].append(strs[i])
        ans = list(hmap.values())
        return ans











