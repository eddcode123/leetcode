from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented as linked lists and returns the sum as a linked list.
        
        Args:
            l1 (ListNode): First linked list.
            l2 (ListNode): Second linked list.
        
        Returns:
            ListNode: Sum represented as a linked list.
        """
        dummy = ListNode()
        current = dummy
        carry = 0

        # Traverse both lists while either has nodes left or there's a carry
        while l1 or l2 or carry:
            # Extract values or use 0 if a list has been fully traversed
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            # Move pointers forward
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
