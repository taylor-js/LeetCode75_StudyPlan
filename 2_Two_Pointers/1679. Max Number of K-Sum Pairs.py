# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        output = 0
        seen = set()

        for x in c:
            if x not in seen and (k - x) in c:
                if x == (k - x):
                    output += c[x] // 2
                else:
                    output += min(c[x], c[k - x])
                seen.add(x)
                seen.add(k - x)

        return output

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    k = 5
    result = sol.maxOperations(nums, k)
    print(result)