# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        frequency = Counter(nums)
        pairs = 0
        for key in frequency.keys():
            a, b = key, k - key
            if a < b:
                pairs += min(frequency[a], frequency[b])
            elif a == b:
                pairs += frequency[a] // 2
        return pairs

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    k = 5
    result = sol.maxOperations(nums, k)
    print(result)