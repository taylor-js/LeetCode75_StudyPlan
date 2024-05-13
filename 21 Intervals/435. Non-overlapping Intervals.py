# https://leetcode.com/problems/non-overlapping-intervals/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
    
        # Sort intervals based on the end times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        end = intervals[0][1]
        count = 0
        
        # Iterate through intervals starting from the second one
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # Current interval overlaps with the previous one, increment count
                count += 1
            else:
                # No overlap, update end to the end of the current interval
                end = intervals[i][1]
        
        return count
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    eoi1 = s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
    print(eoi1) # Output: 1
    # Example 2
    eoi2 = s.eraseOverlapIntervals([[1,2],[1,2],[1,2]])
    print(eoi2) # Output: 2
    # Example 3
    eoi3 = s.eraseOverlapIntervals([[1,2],[2,3]])
    print(eoi3) # Output: 0