# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(set(c.values())) == len(c)
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    arr1 = [1,2,2,1,1,3]
    uo1 = s.uniqueOccurrences(arr1)
    print(uo1)
    # Example 2
    arr2 = [1,2]
    uo2 = s.uniqueOccurrences(arr2)
    print(uo2)
    # Example 3
    arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
    uo3 = s.uniqueOccurrences(arr3)
    print(uo3)