# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(set(c.values())) == len(c)
    
if __name__ == "__main__":
    # Input: arr = [1,2,2,1,1,3]
    sol = Solution()
    output_1 = sol.uniqueOccurrences([1,2,2,1,1,3])
    print(output_1)
    # Output: True

    # Input: arr = [1,2]
    output_2 = sol.uniqueOccurrences([1,2])
    print(output_2)
    # Output: False

    # Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
    output_3 = sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
    print(output_3)
    # Output: True
