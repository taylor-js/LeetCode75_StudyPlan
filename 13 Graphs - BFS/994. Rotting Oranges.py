# https://leetcode.com/problems/rotting-oranges/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()  # Create a queue to hold positions of rotten oranges using deque for efficient pop and append operations.
        time, fresh = 0, 0  # Initialize time to track the minutes and fresh to count fresh oranges.
        rows, cols = len(grid), len(grid[0])  # Determine the size of the grid.
        
        # Traverse the grid to initialize the queue with rotten oranges and count fresh oranges.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1  # Increment the count for each fresh orange found.
                elif grid[r][c] == 2:
                    queue.append((r, c))  # Add the position of each rotten orange to the queue.

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))  # Directions arrays for moving in 4 directions (right, left, down, up).

        # Process the queue until it's empty or there are no fresh oranges left.
        while queue and fresh:
            for _ in range(len(queue)):  # Process each level of the queue (all oranges that will rot in the current minute).
                r, c = queue.popleft()  # Pop the current rotten orange's position from the queue.
                for dr, dc in directions:  # Explore all four adjacent cells.
                    row, col = r + dr, c + dc  # Calculate the new position.
                    # Check if the new position is within bounds and the orange there is fresh.
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2  # Mark the orange as rotten.
                        queue.append((row, col))  # Add the new rotten orange's position to the queue.
                        fresh -= 1  # Decrease the count of fresh oranges.
            time += 1  # Increment the time after processing all current oranges.

        return time if fresh == 0 else -1  # Return the total time if all fresh oranges are rotten; otherwise, return -1.

if __name__ == "__main__":
    s = Solution()
    # Example 1
    grid1 = [[2,1,1],
             [1,1,0],
             [0,1,1]]
    or1 = s.orangesRotting(grid1)
    print(or1)
    # Example 2
    grid2 = [[2,1,1],
             [0,1,1],
             [1,0,1]]
    or2 = s.orangesRotting(grid2)
    print(or2)
    # Example 3
    grid3 = [[0,2]]
    or3 = s.orangesRotting(grid3)
    print(or3)