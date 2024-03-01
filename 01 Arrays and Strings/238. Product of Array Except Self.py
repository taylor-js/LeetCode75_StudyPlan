# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    nums1 = [1,2,3,4]
    pes1 = sol.productExceptSelf(nums1)
    print(pes1)
    # Example 2
    nums2 = [-1,1,0,-3,3]
    pes2 = sol.productExceptSelf(nums2)
    print(pes2)