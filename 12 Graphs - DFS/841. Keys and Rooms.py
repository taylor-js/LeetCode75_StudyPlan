# https://leetcode.com/problems/keys-and-rooms/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room):
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    dfs(i)
        dfs(0)
        return len(visited) == len(rooms)
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    rooms1 = [[1],[2],[3],[]]
    cvar1 = s.canVisitAllRooms(rooms1)
    print(cvar1)
    # Example 2
    rooms2 = [[1,3],[3,0,1],[2],[0]]
    cvar2 = s.canVisitAllRooms(rooms2)
    print(cvar2)