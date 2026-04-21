class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        self.fresh = 0
        
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                # To avoid going over grid again, keep count of fresh to see are all rotten at the end or not!
                elif grid[r][c] == 1:
                    self.fresh += 1

        def addRotten(row, col):
            # Can be grid[row][col] != 1 meaning rotten(2) or empty(0), but rottens are already in visit so equivalent
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0 or (row, col) in visit:
                return 0
            q.append((row, col))
            visit.add((row, col))
            grid[row][col] = 2
            self.fresh -= 1
            return 1 

        minute = 0
        moved = True
        while q and (moved or minute==0):
            moved = False
            #Freeze size of the queue at the start of the minute, Only process those nodes
            #Newly added nodes go to the next minute
            for i in range(len(q)):
                r, c = q.popleft()
   
                up = addRotten(r+1, c)
                down = addRotten(r-1, c)
                right = addRotten(r, c+1)
                left = addRotten(r, c-1)
                moved = up or down or right or left or moved
            if moved:
                minute += 1
        
        if self.fresh != 0:
            return -1
        else:
            return minute
        