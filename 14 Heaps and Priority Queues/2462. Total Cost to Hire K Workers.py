# https://leetcode.com/problems/total-cost-to-hire-k-workers/description/?envType=study-plan-v2&envId=leetcode-75

import heapq
from typing import List

class Solution:
    def totalCost(self, worker_costs: List[int], k: int, candidates: int) -> int:
        i = 0
        j = len(worker_costs) - 1
        min_heap_left = []
        min_heap_right = []
        total_cost = 0
        while k > 0:
            while i <= j and len(min_heap_left) < candidates:
                heapq.heappush(min_heap_left, worker_costs[i])
                i += 1
            while i <= j and len(min_heap_right) < candidates:
                heapq.heappush(min_heap_right, worker_costs[j])
                j -= 1
            cost_left = min_heap_left[0] if min_heap_left else float('inf')
            cost_right = min_heap_right[0] if min_heap_right else float('inf')
            if cost_left <= cost_right:
                total_cost += cost_left
                heapq.heappop(min_heap_left)
            else:
                total_cost += cost_right
                heapq.heappop(min_heap_right)
            k -= 1
        return total_cost

if __name__ == "__main__":
    s = Solution()
    # Example 1
    costs1 = [17,12,10,2,7,2,11,20,8]
    k1 = 3
    candidates1 = 4
    tc1 = s.totalCost(costs1, k1, candidates1)
    print(tc1)
    # Example 2
    costs2 = [1,2,4,1]
    k2 = 3
    candidates2 = 3
    tc2 = s.totalCost(costs2, k2, candidates2)
    print(tc2)
