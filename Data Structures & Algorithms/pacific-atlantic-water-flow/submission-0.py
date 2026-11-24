class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pac = [[0 for _ in range(m)] for _ in range(n)]
        atl = [[0 for _ in range(m)] for _ in range(n)]
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]

        def dfs(r,c,seen):
            seen[r][c] = 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m and heights[nr][nc]>=heights[r][c] and not seen[nr][nc]:
                    dfs(nr,nc,seen)
        ans = []
        for i in range(n):
            dfs(i,0,pac)
        for i in range(m):
            dfs(0,i,pac)

        for j in range(n):
            dfs(j,m-1,atl)
        for j in range(m):
            dfs(n-1,j,atl)

        for i in range(n):
            for j in range(m):
                if  atl[i][j] == 1 and pac[i][j] == 1:
                    ans.append([i,j])
        return ans
