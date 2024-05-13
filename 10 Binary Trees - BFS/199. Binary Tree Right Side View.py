# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class sution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])
        while queue:
            rightSide = None
            queueLen = len(queue)
            for _ in range(queueLen):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:
                result.append(rightSide.val)
        return result
    
if __name__ == "__main__":
    s = sution()
    # Example 1 Tree 1: [1, 2, 3, None, 5, None, 4]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = None
    root1.left.right = TreeNode(5)
    root1.right.left = None
    root1.right.right = TreeNode(4)
    rsv1 = s.rightSideView(root1)
    print(rsv1)

    # Example 2 Tree 2: [1, None, 3]
    root2 = TreeNode(1)
    root2.left = None
    root2.right = TreeNode(3)
    rsv2 = s.rightSideView(root2)
    print(rsv2)

    # Example 3 Tree 3: []
    root3 = None
    rsv3 = s.rightSideView(root3)
    print(rsv3)