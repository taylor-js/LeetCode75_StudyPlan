# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        operations_count = 0
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                operations_count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return operations_count

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    k = 5
    result = sol.maxOperations(nums, k)
    print(result)