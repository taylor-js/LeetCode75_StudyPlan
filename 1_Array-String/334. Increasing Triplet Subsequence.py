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