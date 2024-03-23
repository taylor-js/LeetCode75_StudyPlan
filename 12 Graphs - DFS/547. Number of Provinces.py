# https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)
        numOfProvinces = 0
        visited = set()
        for start in range(len(isConnected)):
            if start not in visited:
                numOfProvinces += 1
                dfs(start)
        return numOfProvinces
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    isConnected1 = [[1,1,0],[1,1,0],[0,0,1]]
    fcm1 = sol.findCircleNum(isConnected1)
    print(fcm1)
    # Example 2
    isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]
    fcm2 = sol.findCircleNum(isConnected2)
    print(fcm2)