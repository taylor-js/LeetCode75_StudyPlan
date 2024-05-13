# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        altitude = 0
        for number in gain:
            altitude += number
            result = max(result, altitude)
        return result
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    gain1 = [-5,1,5,0,-7]
    la1 = s.largestAltitude(gain1)
    print(la1)
    # Example 2
    gain2 = [-4,-3,-2,-1,4,3,2]
    la2 = s.largestAltitude(gain2)
    print(la2)