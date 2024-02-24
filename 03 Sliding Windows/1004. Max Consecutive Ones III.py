# https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_consecutives = 0
        for right, num in enumerate(nums):
            k -= 1 - num
            if k < 0:
                k += 1 - nums[left]
                left += 1
            else:
                max_consecutives = max(max_consecutives, right - left + 1)
        return max_consecutives
    
if __name__ == "__main__":
    # Example 1
    sol = Solution()
    nums1 = [1,1,1,0,0,0,1,1,1,1,0]
    k1 = 2
    lo1 = sol.longestOnes(nums1, k1)
    print(lo1)

    nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k2 = 3
    lo2 = sol.longestOnes(nums2, k2)
    print(lo2)