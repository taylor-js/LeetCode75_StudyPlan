# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = []
        maximum = max(candies)
        
        for c in candies:
            if c + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        
        return result

if __name__ == "__main__":
    s = Solution()
    # Example 1
    candies1 = [2,3,5,1,3]
    extraCandies1 = 3
    kwc1 = s.kidsWithCandies(candies1, extraCandies1)
    print(kwc1)
    # Example 2
    candies2 = [4,2,1,1,2]
    extraCandies2 = 1
    kwc2 = s.kidsWithCandies(candies2, extraCandies2)
    print(kwc2)