# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Create a set 'edges' to store all connections between cities.
        edges = {(a, b) for a, b in connections}
        
        # Create a dictionary 'neighbors' to store neighbors of each city.
        neighbors = {city: [] for city in range(n)}
        
        # Create an empty set 'visit' to store visited cities during traversal.
        visit = set()
        
        # Initialize 'changes' counter to keep track of directional changes.
        changes = 0
        
        # Populate the 'neighbors' dictionary based on the given connections.
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        # Define a Depth First Search (DFS) function to traverse cities recursively.
        def dfs(city):
            nonlocal edges, neighbors, visit, changes
            
            # Iterate through the neighbors of the current city.
            for neighbor in neighbors[city]:
                # Skip if the neighbor has already been visited.
                if neighbor in visit:
                    continue
                
                # Check if the connection is from the neighbor to the current city.
                # If not, it implies a directional change is needed.
                if (neighbor, city) not in edges:
                    changes += 1
                
                # Mark the neighbor as visited and recursively call DFS on it.
                visit.add(neighbor)
                dfs(neighbor)
        
        # Start DFS from city 0.
        visit.add(0)
        dfs(0)
        
        # Return the total number of directional changes needed.
        return changes

if __name__ == "__main__":
    s = Solution()
    # Example 1
    n1 = 6
    connections1 = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    mr1 = s.minReorder(n1, connections1)
    print(mr1)
    # Example 2
    n2 = 5
    connections2 = [[1,0],[1,2],[3,2],[3,4]]
    mr2 = s.minReorder(n2, connections2)
    print(mr2)
    # Example 3
    n3 = 3
    connections3 = [[1,0],[2,0]]
    mr3 = s.minReorder(n3, connections3)
    print(mr3)