from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
    
if __name__ == "__main__":
    sol = Solution()
    cost1 = [10,15,20]
    mccs1 = sol.minCostClimbingStairs(cost1)
    print(mccs1)
    cost2 = [1,100,1,1,1,100,1,1,100,1]
    mccs2 = sol.minCostClimbingStairs(cost2)
    print(mccs2)