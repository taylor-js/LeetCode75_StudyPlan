# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    nums1 = [1,2,3,1]
    r1 = sol.rob(nums1)
    print(r1)
    # Example 2
    nums2 = [2,7,9,3,1]
    r2 = sol.rob(nums2)
    print(r2)