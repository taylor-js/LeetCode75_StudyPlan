# https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1
        
        def dfs(node, root_sum):
            if not node:
                return
            root_sum += node.val
            self.total += self.lookup[root_sum]
            self.lookup[root_sum + targetSum] += 1
            dfs(node.left, root_sum)
            dfs(node.right, root_sum)
            self.lookup[root_sum + targetSum] -= 1

        dfs(root, 0)
        return self.total


if __name__ == "__main__":
    s = Solution()
    # Example 1
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(-3)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(2)
    root1.right.right = TreeNode(11)
    root1.left.left.left = TreeNode(3)
    root1.left.left.right = TreeNode(-2)
    root1.left.right.right = TreeNode(1)
    targetSum1 = 8
    ps1 = s.pathSum(root1, targetSum1)
    print(ps1)
    # Example 2
    root2 = TreeNode(5)
    root2.left = TreeNode(4)
    root2.right = TreeNode(8)
    root2.left.left = TreeNode(11)
    root2.left.left.left = TreeNode(7)
    root2.left.left.right = TreeNode(2)
    root2.right.left = TreeNode(13)
    root2.right.right = TreeNode(4)
    root2.right.right.left = TreeNode(5)
    root2.right.right.right = TreeNode(1)
    targetSum2 = 22
    ps2 = s.pathSum(root2, targetSum2)
    print(ps2)