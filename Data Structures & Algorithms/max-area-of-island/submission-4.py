class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        # Assuming grid is not corrupted
        rows, cols = len(grid), len(grid[0])
        areaMax = 0

        def dfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            if (r, c) in visited or not((0 <= r < rows and 0 <= c < cols and grid[r][c] == 1)):
                return 0
            visited.add((r, c))
            return 1 +  dfs(r+directions[0][0], c+directions[0][1]) + \
                        dfs(r+directions[1][0], c+directions[1][1]) + \
                        dfs(r+directions[2][0], c+directions[2][1]) + \
                        dfs(r+directions[3][0], c+directions[3][1])

            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    areaMax = max(areaMax, dfs(r, c))
        return areaMax
        