class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from collections import defaultdict,deque
        present = [False] * 26
        for word in words:
            for ch in word:
                present[ord(ch)-ord('a')] = True
        #genereating adj Graph
        adj = defaultdict(set)
        indegree = [0] * 26
        for i in range(len(words)-1):
            s1 = words[i]
            s2 = words[i+1]
            min_len = min(len(s1),len(s2))
            if len(s1) > len(s2) and s1.startswith(s2):
                return ""
            for j in range(min_len):
                if s1[j]!=s2[j]:
                    u = ord(s1[j]) - ord('a')
                    v = ord(s2[j]) - ord('a')
                    if v not in adj[u]:
                        indegree[v]+=1
                        adj[u].add(v)
                    break
        ans = []
        q = deque()
        for i in range(len(indegree)):
            if present[i] and indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for neigh in adj[node]:
                indegree[neigh]-=1
                if indegree[neigh] == 0:
                    q.append(neigh)
            ans.append(chr(node + ord('a')))
        
        if len(ans) != sum(present):
            return ""
        return ''.join(ans)
            
        
        