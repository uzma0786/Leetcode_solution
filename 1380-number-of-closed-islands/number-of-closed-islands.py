from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(sr, sc):
            stack = [(sr, sc)]
            grid[sr][sc] = 1
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        stack.append((nr, nc))

        # remove border-connected land
        for r in range(m):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][n-1] == 0:
                dfs(r, n-1)
        for c in range(n):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[m-1][c] == 0:
                dfs(m-1, c)

        closed = 0
        for r in range(1, m-1):
            for c in range(1, n-1):
                if grid[r][c] == 0:
                    closed += 1
                    dfs(r, c)
        return closed