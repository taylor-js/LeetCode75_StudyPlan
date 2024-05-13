# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        for s in spells:
            left, right = 0, len(potions) - 1
            index = len(potions)
            while left <= right:
                mid = (left + right) // 2
                if s * potions[mid] >= success:
                    right = mid - 1
                    index = mid
                else:
                    left = mid + 1
            result.append(len(potions) - index)
        return result

if __name__ == "__main__":
    s = Solution()
    # Example 1
    spells1 = [5,1,3]
    potions1 = [1,2,3,4,5]
    success1 = 7
    sp1 = s.successfulPairs(spells1,potions1,success1)
    print(sp1)
    # Example 2
    spells2 = [3,1,2]
    potions2 = [8,5,8]
    success2 = 16
    sp2 = s.successfulPairs(spells2,potions2,success2)
    print(sp2)