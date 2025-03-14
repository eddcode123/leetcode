from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted linked list.

        Args:
            list1 (Optional[ListNode]): The head of the first sorted linked list.
            list2 (Optional[ListNode]): The head of the second sorted linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        """
        # Create a dummy node to act as the start of the merged list.
        dummy = ListNode()
        # Pointer to the current node in the merged list.
        current = dummy

        # Traverse both lists until one of them is empty.
        while list1 and list2:
            # Link the node with the smaller value to the merged list.
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Move the pointer forward in the merged list.
            current = current.next

        # If any nodes remain in list1, append them to the merged list.
        if list1:
            current.next = list1
        # If any nodes remain in list2, append them to the merged list.
        else:
            current.next = list2

        # Return the head of the merged list, skipping the dummy node.
        return dummy.next