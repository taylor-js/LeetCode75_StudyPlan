# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right

if __name__ == "__main__":
    s = Solution()

    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    root1.left.left.left = TreeNode(None)
    root1.left.left.right = TreeNode(None)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    p1 = TreeNode(5)
    q1 = TreeNode(1)
    lca1 = s.lowestCommonAncestor(root1, p1, q1)
    print(lca1.val)  # Expected output: 3

    # Example 2
    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(2)
    root2.right.left = TreeNode(0)
    root2.right.right = TreeNode(8)
    root2.left.left.left = TreeNode(None)
    root2.left.left.right = TreeNode(None)
    root2.left.right.left = TreeNode(7)
    root2.left.right.right = TreeNode(4)
    p2 = TreeNode(5)
    q2 = TreeNode(4)
    lca2 = s.lowestCommonAncestor(root2, p2, q2)
    print(lca2.val)  # Expected output: 5

    # Example 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    p3 = TreeNode(1)
    q3 = TreeNode(2)
    lca3 = s.lowestCommonAncestor(root3, p3, q3)
    print(lca3.val)  # Expected output: 1
