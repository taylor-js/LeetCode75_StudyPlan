# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, count_zeros, max_length = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zeros += 1
            while count_zeros > 1:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
            max_length = max(max_length, right - left)
        return max_length

if __name__ == "__main__":
    # Input: nums = [1,1,0,1]
    sol = Solution()
    output_1 = sol.longestSubarray([1,1,0,1])
    print(output_1)
    # Output: 3

    # Input: nums = [0,1,1,1,0,1,1,0,1]
    output_2 = sol.longestSubarray([0,1,1,1,0,1,1,0,1])
    print(output_2)
    # Output: 5