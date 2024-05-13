# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # If mid element is less than the next element, peak must be in right half
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # Else, the peak is in the left half
            else:
                right = mid
        # When left == right, we have found a peak element
        return left
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    nums1 = [1,2,3,1]
    fpe1 = s.findPeakElement(nums1)
    print(fpe1)
    # Example 2
    nums2 = [1,2,1,3,5,6,4]
    fpe2 = s.findPeakElement(nums2)
    print(fpe2)