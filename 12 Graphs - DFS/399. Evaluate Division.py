# https://leetcode.com/problems/evaluate-division/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Initialize a defaultdict to represent the graph where keys are nodes and values are dictionaries of neighbors and edge weights
        graph = defaultdict(dict)

        # Build the graph based on provided equations and values
        for (numerator, denominator), value in zip(equations, values):
            # Add the current equation and its reciprocal to the graph
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value

        # Define a depth-first search function to find a path and calculate the result
        def dfs(start, end, visited):
            # If either start or end node is not in the graph, return -1.0 indicating impossibility
            if start not in graph or end not in graph:
                return -1.0
            # If there exists a direct edge from start to end, return its weight
            if end in graph[start]:
                return graph[start][end]
            
            # Add the start node to the visited set to avoid revisiting it
            visited.add(start)
            # Iterate over neighbors of the start node
            for neighbor, value in graph[start].items():
                # If the neighbor has not been visited yet, recursively call dfs on it
                if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    # If a valid result is obtained from the neighbor, return the multiplication of current edge weight and result
                    if res != -1.0:
                        return value * res
            # If no valid result is found, return -1.0
            return -1.0

        # Initialize a list to store the results of queries
        results = []
        # Iterate over each query in the queries list
        for query in queries:
            numerator, denominator = query
            # Call dfs function to find the result for the current query and append it to results list
            result = dfs(numerator, denominator, set())
            results.append(result)
        
        # Return the list of results for all queries
        return results
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    equations1 = [["a","b"],["b","c"]]
    values1 = [2.0,3.0]
    queries1 = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ce1 = s.calcEquation(equations1,values1,queries1)
    print(ce1)
    # Example 2
    equations2 = [["a","b"],["b","c"],["bc","cd"]]
    values2 = [1.5,2.5,5.0]
    queries2 = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    ce2 = s.calcEquation(equations2,values2,queries2)
    print(ce2)
    # Example 3
    equations3 = [["a","b"]]
    values3 = [0.5]
    queries3 = [["a","b"],["b","a"],["a","c"],["x","y"]]
    ce3 = s.calcEquation(equations3,values3,queries3)
    print(ce3)