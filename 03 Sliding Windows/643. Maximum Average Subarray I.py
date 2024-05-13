# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    # Define a class called 'Solution'.
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Define a method called 'findMaxAverage' within the class.
        # It takes a list of integers 'nums' and an integer 'k' as inputs,
        # and it returns a floating-point number.

        # Initialize 'current_sum' to be the sum of the first 'k' elements in 'nums'.
        current_sum = sum(nums[:k])
        
        # Initialize 'max_sum' with the initial 'current_sum'.
        max_sum = current_sum

        # Iterate from the 'k'-th element to the end of the 'nums' list.
        for i in range(k, len(nums)):
            # Update 'current_sum' by adding the current element
            # and subtracting the element 'k' positions ago.
            current_sum = current_sum + nums[i] - nums[i - k]
            
            # Update 'max_sum' to be the maximum of the current 'max_sum'
            # and the updated 'current_sum'.
            max_sum = max(max_sum, current_sum)

        # Calculate the maximum average by dividing 'max_sum' by 'k'.
        max_average = max_sum / k

        # Return the calculated maximum average.
        return max_average
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    nums1 = [1,12,-5,-6,50,3]
    k1 = 4
    fma1 = s.findMaxAverage(nums1, k1)
    print(fma1)
    # Example 2
    nums2 = [5]
    k2 = 1
    fma2 = s.findMaxAverage(nums2, k2)
    print(fma2)