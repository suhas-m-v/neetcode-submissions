class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        seen = [[0 for _ in range(m)] for _ in range(n)]
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        def dfs(r,c):
            seen[r][c] = 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m and board[nr][nc] == 'O' and not seen[nr][nc]:
                    dfs(nr,nc)

        for i in range(n):
            if board[i][0] == 'O' and not seen[i][0]:
                dfs(i,0)
            if board[i][m-1] == 'O' and not seen[i][m-1]:
                dfs(i,m-1)
        
        for j in range(m):
            if board[0][j] == 'O' and not seen[0][j]:
                dfs(0,j)
            if board[n-1][j] == 'O' and not seen[n-1][j]:
                dfs(n-1,j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not seen[i][j]:
                    board[i][j] = 'X'