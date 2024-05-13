# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        def dfs(node, left, right):
            self.maximum = max(self.maximum, left, right)
            if node.left:
                dfs(node.left, right + 1, 0)
            if node.right:
                dfs(node.right, 0, left + 1)
        dfs(root, 0, 0)
        return self.maximum
    
if __name__ == "__main__":
    s = Solution()
    # Example 1: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
    root1 = TreeNode(1)
    root1.left = TreeNode(None)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(1)
    root1.right.left = TreeNode(None)
    root1.right.right = TreeNode(None)
    root1.left.left.left = TreeNode(1)
    root1.left.left.right = TreeNode(1)
    root1.left.right.left = TreeNode(None)
    root1.left.right.right = TreeNode(1)
    root1.right.left.left = TreeNode(None)
    root1.right.left.right = TreeNode(None)
    root1.right.right.left = TreeNode(None)
    root1.right.right.right = TreeNode(1)
    e1tn = s.longestZigZag(root1)
    print(e1tn)
    # Example 2: root = [1,1,1,null,1,null,null,1,1,null,1]
    root2 = TreeNode(1)
    root2.left = TreeNode(1)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(None)
    root2.left.right = TreeNode(1)
    root2.right.left = TreeNode(None)
    root2.right.right = TreeNode(None)
    root2.left.right.left = TreeNode(1)
    root2.left.right.right = TreeNode(None)
    root2.left.right.left.left = TreeNode(1)
    root2.left.right.left.right = TreeNode(None)
    root2.right.right.left = TreeNode(None)
    root2.right.right.right = TreeNode(1)
    e2 = s.longestZigZag(root2)
    print(e2)
    # Example 3: root = [1]
    root3 = TreeNode(1)
    e3 = s.longestZigZag(root3)
    print(e3)
