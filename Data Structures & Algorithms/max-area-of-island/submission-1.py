class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        # Assuming grid is not corrupted
        rows, cols = len(grid), len(grid[0])
        areaMax = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            island_curr = set()
            island_curr.add((r, c))
            q.append((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                row, col = q.popleft() 
                for d in directions:
                    r, c = row + d[0], col + d[1]
                    if  0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited:
                        visited.add((r,c))
                        island_curr.add((r, c))
                        q.append((r, c))

            return len(island_curr)
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    areaMax = max(areaMax, bfs(r, c))
        return areaMax
        