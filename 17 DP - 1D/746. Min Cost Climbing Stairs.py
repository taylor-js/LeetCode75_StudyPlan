# https://leetcode.com/problems/min-cost-climbing-stairs/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    mccs1 = s.minCostClimbingStairs([10,15,20])
    print(mccs1)
    # Example 2
    mccs2 = s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
    print(mccs2)