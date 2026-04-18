class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        
        n_rows, n_cols = len(grid), len(grid[0])
        self.visited = set()
        n_islands = 0

        def bfs(r, c):
            q = collections.deque()
            self.visited.add((r,c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dir in directions: 
                    r, c = row + dir[0], col + dir[1]
                    if  0 <= r < n_rows and \
                        0 <= c < n_cols and \
                       (r, c) not in self.visited and \
                       grid[r][c] == "1": 

                       q.append((r, c))
                       self.visited.add((r, c))

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "1" and (r,c) not in self.visited:
                    bfs(r, c)
                    n_islands += 1
        return n_islands