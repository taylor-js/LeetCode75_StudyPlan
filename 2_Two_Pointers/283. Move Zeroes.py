# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_index = 0
        current_index = 0

        while current_index < len(nums):
            if nums[current_index] != 0:
                nums[non_zero_index], nums[current_index] = nums[current_index], nums[non_zero_index]
                non_zero_index += 1
            current_index += 1
            
        return nums

if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    result = sol.moveZeroes(nums)
    print(result)