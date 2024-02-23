# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0
        rows = defaultdict(int)
        for row in range(len(grid)):
            rows[tuple(grid[row])] += 1
        for j in range(len(grid)):
            column = tuple(grid[i][j] for i in range(len(grid)))
            result += rows[column]
        return result
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    e1 = sol.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]])
    print(e1)
    # Example 2
    e2 = sol.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
    print(e2)