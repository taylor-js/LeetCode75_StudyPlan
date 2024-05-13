# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set, nums2Set = set(nums1), set(nums2)
        result1, result2 = set(), set()
        for n in nums1:
            if n not in nums2Set:
                result1.add(n)
        for n in nums2:
            if n not in nums1Set:
                result2.add(n)
        return [list(result1), list(result2)]
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    fd1 = s.findDifference(nums1, nums2)
    print(fd1)
    # Example 2
    nums3 = [1,2,3,3]
    nums4 = [1,1,2,2]
    fd2 = s.findDifference(nums3, nums4)
    print(fd2)