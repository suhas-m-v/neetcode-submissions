class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = [[0 for _ in range(m)] for _ in range(n)]
        cnt = 0
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        def dfs(r,c):
            seen[r][c] = 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m and grid[nr][nc] == "1" and not seen[nr][nc]:
                    dfs(nr,nc)
            

        for i in range(n):
            for j in range(m):
                if  grid[i][j] == "1" and not seen[i][j]:
                    dfs(i,j)
                    cnt+=1
        return cnt
        
