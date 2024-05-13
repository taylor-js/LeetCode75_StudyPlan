# https://leetcode.com/problems/koko-eating-bananas/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Function to check if Koko can eat all bananas at a certain speed within h hours
        def can_finish(k):
            return sum((pile - 1) // k + 1 for pile in piles) <= h

        # Binary search for the minimum eating speed
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    s = Solution()
    # Example 1
    piles1 = [3,6,7,11]
    h1 = 8
    mes1 = s.minEatingSpeed(piles1, h1)
    print(mes1)
    # Example 2
    piles2 = [30,11,23,4,20]
    h2 = 5
    mes2 = s.minEatingSpeed(piles2, h2)
    print(mes2)
    # Example 3
    piles3 = [30,11,23,4,20]
    h3 = 6
    mes3 = s.minEatingSpeed(piles3, h3)
    print(mes3)