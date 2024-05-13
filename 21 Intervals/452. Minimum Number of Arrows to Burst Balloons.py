# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
    
        # Sort points based on the end coordinates
        points.sort(key=lambda x: x[1])
        
        # Initialize the number of arrows and the position of the first arrow
        arrows = 1
        current_arrow_position = points[0][1]
        
        # Go through the sorted balloons
        for xstart, xend in points:
            # If the start of the current balloon is greater than the position of the last arrow
            # It means we need a new arrow
            if xstart > current_arrow_position:
                arrows += 1
                current_arrow_position = xend  # Place new arrow at the end of the current balloon
        
        return arrows
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    fmas1 = s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
    print(fmas1) # Output: 2
    # Example 2
    fmas2 = s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
    print(fmas2) # Output: 4
    # Example 3
    fmas3 = s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
    print(fmas3) # Output: 2