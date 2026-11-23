from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque([])
        ans = -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0<=nr<n and 0<=nc<m and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            ans+=1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: 
                    return -1
        return max(ans,0)