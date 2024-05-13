# https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return head
        # Initialize two separate linked lists for odd and even indices
        odd_head = ListNode(0)
        even_head = ListNode(0)
        odd_pointer = odd_head
        even_pointer = even_head
        # Initialize a variable to keep track of whether the current node is at an odd or even index
        is_odd = True
        # Traverse the original linked list
        while head:
            # Depending on whether the current index is odd or even, add the node to the corresponding list
            if is_odd:
                odd_pointer.next = head
                odd_pointer = odd_pointer.next
            else:
                even_pointer.next = head
                even_pointer = even_pointer.next
            # Switch the index type for the next iteration
            is_odd = not is_odd
            # Move to the next node in the original linked list
            head = head.next
        # Connect the last node of the odd list to the first node of the even list
        odd_pointer.next = even_head.next
        # Set the next pointer of the last node in the even list to None to terminate the list
        even_pointer.next = None
        # Return the reorganized linked list with odd indices followed by even indices
        return odd_head.next
    
    def print_linkedlist(self, node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        print(*values)
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    oel1 = s.oddEvenList(head1)
    s.print_linkedlist(oel1)
    # Example 2
    head2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    oel2 = s.oddEvenList(head2)
    s.print_linkedlist(oel2)
    