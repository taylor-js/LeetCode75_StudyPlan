# https://leetcode.com/problems/combination-sum-iii/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, remain, path):
            if remain == 0 and len(path) == k:
                result.append(path[:])
                return
            elif remain < 0 or len(path) > k:
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(i+1, remain-i, path)
                path.pop()
        result = []
        backtrack(1, n, [])
        return result

if __name__ == "__main__":
    s = Solution()
    fc1 = s.combinationSum3(3, 7)
    print(fc1)
    fc2 = s.combinationSum3(3, 9)
    print(fc2)
    fc3 = s.combinationSum3(4, 1)
    print(fc3)