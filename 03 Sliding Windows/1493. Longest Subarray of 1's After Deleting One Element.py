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
    sol = Solution()
    # Example 1
    nums1 = [1,1,0,1]
    ls1 = sol.longestSubarray(nums1)
    print(ls1)
    # Example 2
    nums2 = [0,1,1,1,0,1,1,0,1]
    ls2 = sol.longestSubarray(nums2)
    print(ls2)
    # Example 3
    nums3 = [1,1,1]
    ls3 = sol.longestSubarray(nums3)
    print(ls3)