from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize a deque to store the coordinates of rotten oranges.
        queue = deque()
        # Initialize time to track the number of minutes and fresh to track the count of fresh oranges.
        time, fresh = 0, 0
        # Get the number of rows and columns in the grid.
        rows, cols = len(grid), len(grid[0])
        # Iterate through the grid to:
        # 1. Count the fresh oranges and increment 'fresh'.
        # 2. Add the coordinates of rotten oranges to the queue.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])
        # Define directions to move in the grid (up, down, left, right).
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Continue the loop until the queue is empty or no fresh oranges are left.
        while queue and fresh > 0:
            # Process all oranges currently in the queue.
            for _ in range(len(queue)):
                # Get the coordinates of the current rotten orange.
                r, c = queue.popleft()
                # Check all four adjacent directions.
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # Skip if out of bounds or the cell is not fresh.
                    if (row < 0 or row == len(grid) or 
                        col < 0 or col == len(grid[0]) or 
                        grid[row][col] != 1):
                        continue
                    # Mark the fresh orange as rotten, update queue, decrement fresh count.
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
            # Increment time after processing all oranges in the current minute.
            time += 1
        # Return the time taken if all fresh oranges are rotten, otherwise return -1.
        return time if fresh == 0 else -1

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    grid1 = [[2,1,1],
             [1,1,0],
             [0,1,1]]
    or1 = sol.orangesRotting(grid1)
    print(or1)
    # Example 2
    grid2 = [[2,1,1],
             [0,1,1],
             [1,0,1]]
    or2 = sol.orangesRotting(grid2)
    print(or2)
    # Example 3
    grid3 = [[0,2]]
    or3 = sol.orangesRotting(grid3)
    print(or3)