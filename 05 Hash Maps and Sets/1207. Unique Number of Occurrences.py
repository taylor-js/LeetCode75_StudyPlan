# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(set(c.values())) == len(c)
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    arr1 = [1,2,2,1,1,3]
    output_1 = sol.uniqueOccurrences(arr1)
    print(output_1)
    # Output: True

    # Example 2
    arr2 = [1,2]
    output_2 = sol.uniqueOccurrences(arr2)
    print(output_2)
    # Output: False

    # Example 3
    arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
    output_3 = sol.uniqueOccurrences()
    print(output_3)
    # Output: True
