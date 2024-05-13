# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first_min = float('inf')
        second_min = float('inf')

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    # Example 1
    nums1 = [1,2,3,4,5]
    it1 = s.increasingTriplet(nums1)
    print(it1)
    # Example 2
    nums2 = [5,4,3,2,1]
    it2 = s.increasingTriplet(nums2)
    print(it2)
    # Example 3
    nums3 = [2,1,5,0,4,6]
    it3 = s.increasingTriplet(nums3)
    print(it3)