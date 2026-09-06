# Problem: Number of Islands
# Status: Accepted
# Language: python3
# Runtime: 255 ms
# Memory: 21.7 MB
# Submitted: 2026-09-05_202529 UTC
# URL: https://leetcode.com/submissions/detail/2132142585/

class Solution:
    def dfs(self, x, y, grid, m, n, visited):
        if int(grid[x][y]) == 0:
            return
        visited[x][y] = 1
        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x+i, y+j
            if 0<=nx<m and 0<=ny<n:
                if visited[nx][ny] == 0:
                    self.dfs(nx, ny, grid, m, n, visited)


    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if int(grid[i][j]) == 1 and visited[i][j] == 0:
                    count += 1
                    
                    self.dfs(i, j, grid, m, n, visited)
        return count
        
