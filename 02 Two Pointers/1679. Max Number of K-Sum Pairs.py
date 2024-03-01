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
    # Example 1
    nums1 = [1,2,3,4]
    k1 = 5
    mo1 = sol.maxOperations(nums1, k1)
    print(mo1)
    # Example 2
    nums2 = [3,1,3,4,3]
    k2 = 6
    mo2 = sol.maxOperations(nums2, k2)
    print(mo2)