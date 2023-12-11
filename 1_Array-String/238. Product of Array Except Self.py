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

# Example usage:
s = Solution()
nums = [1, 2, 3, 4]
result = s.productExceptSelf(nums)
print(result)  # Output: [24, 12, 8, 6]