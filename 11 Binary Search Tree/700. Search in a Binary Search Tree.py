# https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

if __name__ == "__main__":
    bst = Solution()
    # Example 1 root = [4,2,7,1,3], val = 2
    root1 = TreeNode(4,
        left=TreeNode(2, 
            left=TreeNode(1),
            right=TreeNode(3)
        ),
        right=TreeNode(7)
    )
    val1 = 2
    result1 = bst.searchBST(root1, val1)
    if result1:
        output1 = [result1.val]
        if result1.left:
            output1.append(result1.left.val)
        else:
            output1.append(None)
        if result1.right:
            output1.append(result1.right.val)
        else:
            output1.append(None)
        print("Output for Example 1:", output1)
    else:
        print("Output for Example 1:", [])
    # Example 2 root = [4,2,7,1,3], val = 5
    root2 = TreeNode(
        4,
        left=TreeNode(
            2,
            left=TreeNode(1),
            right=TreeNode(3)
        ),
        right=TreeNode(7)
    )
    val2 = 5
    result2 = bst.searchBST(root2, val2)
    if result2:
        output2 = [result2.val]
        if result2.left:
            output2.append(result2.left.val)
        else:
            output2.append(None)
        if result2.right:
            output2.append(result2.right.val)
        else:
            output2.append(None)
        print("Output for Example 2:", output2)
    else:
        print("Output for Example 2:", [])
