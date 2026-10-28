class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        

        temp=[]
        for i in range(n):
            for j in range(m):
                temp.append(grid[i][j])
        ans = [[0] * m for _ in range(n)]
        k = k%len(temp)
        temp = temp[-k:] + temp[:-k]
        
        for r in range(n):
            for c in range(m):
                ans[r][c] = temp[r * m + c]
        return ans