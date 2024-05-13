# https://leetcode.com/problems/daily-temperatures/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # This will store the indices of the temperatures

        for i in range(n):
            # Check if the current temperature is greater than the temperatures corresponding to the indices in the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Pop the index from the stack
                index = stack.pop()
                # Calculate the number of days until a warmer temperature
                answer[index] = i - index
            # Push the current index onto the stack
            stack.append(i)

        return answer
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    temperatures1 = [73,74,75,71,69,72,76,73]
    dt1 = s.dailyTemperatures(temperatures1)
    print(dt1)
    # Example 2
    temperatures2 = [30,40,50,60]
    dt2 = s.dailyTemperatures(temperatures2)
    print(dt2)
    # Example 3
    temperatures3 = [30,60,90]
    dt3 = s.dailyTemperatures(temperatures3)
    print(dt3)