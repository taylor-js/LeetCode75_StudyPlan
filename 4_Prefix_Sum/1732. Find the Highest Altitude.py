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
    # Input: gain = [-5,1,5,0,-7]
    sol = Solution()
    output_1 = sol.largestAltitude([-5,1,5,0,-7])
    print(output_1)
    # Output: 1

    # Input: gain = [-4,-3,-2,-1,4,3,2]
    output_2 = sol.largestAltitude([-4,-3,-2,-1,4,3,2])
    print(output_2)
    # Output: 0
