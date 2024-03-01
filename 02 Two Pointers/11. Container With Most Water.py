# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            result = max(result, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return result

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    height1 = [1,8,6,2,5,4,8,3,7]
    ma1 = sol.maxArea(height1)
    print(ma1)
    # Example 2
    height2 = [1,1]
    ma2 = sol.maxArea(height2)
    print(ma2)