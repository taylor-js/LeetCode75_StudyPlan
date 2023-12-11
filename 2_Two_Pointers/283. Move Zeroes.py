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