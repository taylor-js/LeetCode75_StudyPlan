# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_counts = Counter(nums)
        operations = 0

        for num in num_counts:
            complement = k - num

            if complement in num_counts and num_counts[complement] > 0:
                num_counts[num] -= 1
                num_counts[complement] -= 1
                operations += 1

        return operations

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    k = 5
    result = sol.maxOperations(nums, k)
    print(result)