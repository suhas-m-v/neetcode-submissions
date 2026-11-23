class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = [[0 for _ in range(m)] for _ in range(n)]
        cnt = float("-inf")
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        def dfs(r,c):
            cnt = 1
            seen[r][c] = 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m and grid[nr][nc] == 1 and not seen[nr][nc]:
                    cnt+= dfs(nr,nc)
            
            return cnt
        for i in range(n):
            for j in range(m):
                if  grid[i][j] == 1 and not seen[i][j]:
                    cnt = max(cnt,dfs(i,j)) 
                    
        if cnt<=0:
            return 0
        return cnt
