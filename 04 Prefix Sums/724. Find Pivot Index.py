# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    nums1 = [1,7,3,6,5,6]
    pi1 = s.pivotIndex(nums1)
    print(pi1)
    # Example 2
    nums2 = [1,2,3]
    pi2 = s.pivotIndex(nums2)
    print(pi2)
    # Example 3
    nums3 = [2,1,-1]
    pi3 = s.pivotIndex(nums3)
    print(pi3)