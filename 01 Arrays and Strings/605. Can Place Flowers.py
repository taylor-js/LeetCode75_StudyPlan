# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
                
        return n <= 0

if __name__ == "__main__":
    s = Solution()
    # Example 1
    flowerbed1 = [1,0,0,0,1]
    n1 = 1
    cpf1 = s.canPlaceFlowers(flowerbed1, n1)
    print(cpf1)
    # Example 2
    flowerbed2 = [1,0,0,0,1]
    n2 = 2
    cpf2 = s.canPlaceFlowers(flowerbed2, n2)
    print(cpf2)