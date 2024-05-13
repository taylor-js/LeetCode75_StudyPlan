# https://leetcode.com/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            # Convert i to binary using bin(), remove the '0b' prefix and count the '1's
            count_of_ones = bin(i).count('1')
            ans.append(count_of_ones)
        return ans

if __name__ == "__main__":
    s = Solution()
    # Example 1
    cb1 = s.countBits(2)
    print(cb1)
    # Example 2
    cb2 = s.countBits(5)
    print(cb2)
