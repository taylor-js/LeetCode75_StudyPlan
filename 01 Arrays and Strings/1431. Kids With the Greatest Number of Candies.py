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
    sol = Solution()
    candies = [2,3,5,1,3]
    extraCandies = 3
    result = sol.kidsWithCandies(candies, extraCandies)
    print(result)