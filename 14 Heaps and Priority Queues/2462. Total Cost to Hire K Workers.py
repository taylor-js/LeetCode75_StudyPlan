# https://leetcode.com/problems/total-cost-to-hire-k-workers/description/?envType=study-plan-v2&envId=leetcode-75

import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost_heap = []

        # Initialize heap with costs of initial candidates
        for i in range(candidates):
            heapq.heappush(cost_heap, (costs[i], 0))
        
        # Initialize heap with costs of trailing candidates
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            heapq.heappush(cost_heap, (costs[i], 1))
        
        total_cost = 0
        left_candidate_index = candidates
        right_candidate_index = len(costs) - candidates - 1

        # Pop the minimum cost candidates and update the heap accordingly
        for _ in range(k):
            min_cost, direction = heapq.heappop(cost_heap)
            total_cost += min_cost
            if left_candidate_index <= right_candidate_index:
                if direction == 0:
                    heapq.heappush(cost_heap, (costs[left_candidate_index], 0))
                    left_candidate_index += 1
                else:
                    heapq.heappush(cost_heap, (costs[right_candidate_index], 1))
                    right_candidate_index -= 1
        
        return total_cost


if __name__ == "__main__":
    sol = Solution()
    # Example 1
    costs1 = [17,12,10,2,7,2,11,20,8]
    k1 = 3
    candidates1 = 4
    tc1 = sol.totalCost(costs1, k1, candidates1)
    print(tc1)
    # Example 2
    costs2 = [1,2,4,1]
    k2 = 3
    candidates2 = 3
    tc2 = sol.totalCost(costs2, k2, candidates2)
    print(tc2)
