# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, n):
            current_sum = current_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        max_average = max_sum / k

        return max_average
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    result = sol.findMaxAverage(nums, k)
    print(result)