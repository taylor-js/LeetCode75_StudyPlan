# https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single

if __name__ == "__main__":
    s = Solution()
    # Example 1
    sn1 = s.singleNumber([2,2,1])
    print(sn1)
    # Example 2
    sn2 = s.singleNumber([4,1,2,1,2])
    print(sn2)
    # Example 3
    sn3 = s.singleNumber([1])
    print(sn3)