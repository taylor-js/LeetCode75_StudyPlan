# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_level = 1
        max_sum = root.val
        queue = deque([root])
        level = 1
        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1
        return max_level
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1: root = [1,7,0,7,-8,null,null]
    root1 = TreeNode(1)
    root1.left = TreeNode(7)
    root1.right = TreeNode(0)
    root1.left.left = TreeNode(7)
    root1.left.right = TreeNode(-8)
    result1 = sol.maxLevelSum(root1)
    print("Example 1 Output:", result1)
    # Example 2: root = [989,null,10250,98693,-89388,null,null,null,-32127]
    root2 = TreeNode(989)
    root2.right = TreeNode(10250)
    root2.right.left = TreeNode(98693)
    root2.right.right = TreeNode(-89388)
    root2.right.right.right = TreeNode(-32127)
    result2 = sol.maxLevelSum(root2)
    print("Example 2 Output:", result2)