# https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                difference = a + stack[-1]
                if difference < 0:
                    stack.pop()
                elif difference > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    asteroids1 = [5,10,-5]
    ac1 = s.asteroidCollision(asteroids1)
    print(ac1)
    # Example 2
    asteroids2 = [8,-8]
    ac2 = s.asteroidCollision(asteroids2)
    print(ac2)
    # Example 3
    asteroids3 = [10,2,-5]
    ac3 = s.asteroidCollision(asteroids3)
    print(ac3)