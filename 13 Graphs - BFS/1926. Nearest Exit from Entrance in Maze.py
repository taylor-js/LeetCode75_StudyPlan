# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Queue initialized with entrance coordinates and distance 0
        queue = deque([(*entrance, 0)])
        # Dimensions of the maze
        rows, cols = len(maze), len(maze[0])
        # Mark the entrance as visited
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            # Pop the first element from the queue
            x, y, steps = queue.popleft()
            # Check if at exit and not entrance
            if (x == 0 or x == rows-1 or y == 0 or y == cols-1) and [x, y] != entrance:
                # If exit found, return the distance
                return steps
            # Iterate through neighboring cells
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # Calculate new coordinates
                i, j = x + dx, y + dy
                # Check if cell is within bounds and not visited
                if 0 <= i < rows and 0 <= j < cols and maze[i][j] == '.':
                    # Mark cell as visited
                    maze[i][j] = '+'
                    # Add cell to the queue with incremented distance
                    queue.append((i, j, steps + 1))
        # If no exit found, return -1
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    maze1 = [["+","+",".","+"],
             [".",".",".","+"],
             ["+","+","+","."]]
    entrance1 = [1,2]
    ne1 = sol.nearestExit(maze1,entrance1)
    print(ne1)
    # Example 2
    maze2 = [["+","+","+"],
             [".",".","."],
             ["+","+","+"]]
    entrance2 = [1,0]
    ne2 = sol.nearestExit(maze2, entrance2)
    print(ne2)
    # Example 3
    maze3 = [[".","+"]]
    entrance3 = [0,0]
    ne3 = sol.nearestExit(maze3, entrance3)
    print(ne3)