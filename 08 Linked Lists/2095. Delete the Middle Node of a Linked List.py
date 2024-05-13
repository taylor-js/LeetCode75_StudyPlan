# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the linked list has only one node or is empty
        if not head.next:
            return None
        
        # Initialize two pointers: slow and fast
        slow = head
        fast = head.next.next

        # Move the fast pointer twice as fast as the slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node by updating the slow pointer's next reference
        slow.next = slow.next.next
        
        # Return the original head of the linked list
        return head
    
    def print_linkedlist(self, node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        print(*values)
    
if __name__ == "__main__":
    s = Solution()
    
    # Example 1
    head1 = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
    dm1 = s.deleteMiddle(head1)
    s.print_linkedlist(dm1)

    # Example 2
    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    dm2 = s.deleteMiddle(head2)
    s.print_linkedlist(dm2)

    # Example 3
    head3 = ListNode(2, ListNode(1))
    dm3 = s.deleteMiddle(head3)
    s.print_linkedlist(dm3)
