# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive DFS
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth1(root.left), self.maxDepth1(root.right))
    
    # Iterative BFS
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    # Pre-order DFS
    def maxDepth3(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        result = 1
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result

if __name__ == "__main__":
    s = Solution()
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    md11 = s.maxDepth1(root1)
    md12 = s.maxDepth2(root1)
    md13 = s.maxDepth3(root1)
    print(md11, md12, md13)
    # Example 2
    root2 = TreeNode(1)
    root2.left = None
    root2.right = TreeNode(2)
    md21 = s.maxDepth1(root2)
    md22 = s.maxDepth2(root2)
    md23 = s.maxDepth3(root2)
    print(md21, md22, md23)