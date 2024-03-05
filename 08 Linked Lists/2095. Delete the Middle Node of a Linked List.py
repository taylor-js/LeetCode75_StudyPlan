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
    
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    head1 = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
    dm1 = sol.deleteMiddle(head1)
    print(head1.val, head1.next.val, head1.next.next.val, head1.next.next.next.val, head1.next.next.next.next.val, head1.next.next.next.next.next.val)

    # Example 2
    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    dm2 = sol.deleteMiddle(head2)
    print(head2.val, head2.next.val, head2.next.next.val)

    # Example 3
    head3 = ListNode(2, ListNode(1))
    dm3 = sol.deleteMiddle(head3)
    print(head3.val)
