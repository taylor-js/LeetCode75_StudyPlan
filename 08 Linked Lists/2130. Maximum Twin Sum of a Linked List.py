# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        result = 0
        while slow:
            result = max(result, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return result
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    head1 = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    ps1 = sol.pairSum(head1)
    print(ps1)
    # Example 2
    head2 = ListNode(4,ListNode(2,ListNode(2,ListNode(3))))
    ps2 = sol.pairSum(head2)
    print(ps2)
    # Example 3
    head3 = ListNode(1, ListNode(100000))
    ps3 = sol.pairSum(head3)
    print(ps3)