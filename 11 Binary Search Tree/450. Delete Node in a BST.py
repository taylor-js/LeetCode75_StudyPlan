# https://leetcode.com/problems/delete-node-in-a-bst/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Find the inorder successor (smallest node in the right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Update the value of the node to be deleted
            root.val = successor.val
            
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, successor.val)
            
        return root
    
    def print_inorder(self, root):
        if root is not None:
            self.print_inorder(root.left)
            print(root.val, end=" ")
            self.print_inorder(root.right)

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    root1 = TreeNode(
        5,
        left=TreeNode(
            3,
            left=TreeNode(2),
            right=TreeNode(4)
        ),
        right=TreeNode(
            6,
            left=None,
            right=TreeNode(7)
        )
    )
    key1 = 3
    sol.deleteNode(root1, key1)
    sol.print_inorder(root1)
    print("\n")
    # Example 2
    root2 = TreeNode(
        5,
        left=TreeNode(
            3,
            left=TreeNode(2),
            right=TreeNode(4)
        ),
        right=TreeNode(
            6,
            left=None,
            right=TreeNode(7)
        )
    )
    key2 = 0
    sol.deleteNode(root2, key2)
    sol.print_inorder(root2)
    print("\n")
    # Example 3
    root3 = None
    key3 = 0
    sol.deleteNode(root3, key3)
    sol.print_inorder(root3)
    print("\n")