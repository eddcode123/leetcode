from typing import Optional
from data_structures import Linkedlist


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(head):
        """
        Determine if the linked list is a cycle

        Args:
            head (ListNode): Pointer to the first node
        
        Returns:
            bool: True if the list has a cycle, False otherwise
        """
        # Edge case: an empty list or a list containing one node
        if not head or not head.next:
            return False
        
        slow = head
        fast = head

        # Traverse the list to detect a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # Cycle detected
            if slow == fast:
                return True
        
        return False
