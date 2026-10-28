class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = set()
        def dfs(r,c):
            seen.add((r,c))
            per = 0
            dr=[-1,0,1,0]
            dc=[0,1,0,-1]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr<0 or nr>=n or nc<0 or nc>=m or grid[nr][nc]==0:
                    per+=1
                elif (nr,nc) not in seen:
                    per+=dfs(nr,nc)
            return per


        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    return dfs(r,c)