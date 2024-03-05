# https://leetcode.com/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def print_linkedlist(self, node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        print(*values)

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    rl1 = sol.reverseList(head1)
    sol.print_linkedlist(rl1)
    # Example 2
    head2 = ListNode(1, ListNode(2))
    rl2 = sol.reverseList(head2)
    sol.print_linkedlist(rl2)
    # Example 3
    head3 = ListNode(None)
    rl3 = sol.reverseList(head3)
    sol.print_linkedlist(rl3)
    