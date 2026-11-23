from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        inf = (2**31) - 1
        seen = [[0 for _ in range(m)] for _ in range(n)]
        q = deque([])
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
                    seen[i][j]=1
        
        while q:
            r,c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c +dc[i]
                if 0<=nr<n and 0<=nc<m and grid[nr][nc] == inf and not seen[nr][nc]:
                    q.append((nr,nc))
                    seen[nr][nc] =1
                    grid[nr][nc] = grid[r][c]+1



