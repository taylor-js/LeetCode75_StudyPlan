# https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            result = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            result += dfs(node.left, maxVal)
            result += dfs(node.right, maxVal)
            return result
        return dfs(root, root.val)
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.left.right = None
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(5)
    gn1 = s.goodNodes(root1)
    print(gn1)

    # Example 2
    root2 = TreeNode(3)
    root2.left = TreeNode(3)
    root2.right = None
    root2.right = TreeNode(4)
    root2.right.left = None
    root2.right.right = TreeNode(2)
    gn2 = s.goodNodes(root2)
    print(gn2)