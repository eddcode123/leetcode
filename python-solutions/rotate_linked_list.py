from typing import Optional
from data_structures import Linkedlist


class ListNode:
    """
    Definition for a singly-linked list node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotates a linked list to the right by k places.

        Args:
            head (Optional[ListNode]): Pointer to the first node of the linked list.
            k (int): Number of positions to rotate the linked list.

        Returns:
            Optional[ListNode]: Pointer to the new head of the rotated linked list.
        """
        # Handle edge cases: no rotation needed if k is 0, the list is empty, or has only one node.
        if k == 0 or not head or not head.next:
            return head

        # Determine the length of the linked list and find the tail node.
        tail = head
        length = 1
        while tail.next:
            length += 1
            tail = tail.next

        # Reduce k to a meaningful value to avoid unnecessary rotations.
        k %= length
        if k == 0:
            return head

        # Find the new tail node after the rotation.
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Update pointers to form the rotated list.
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head


# test case
def print_linked_list(head: ListNode):
    if head:
        temp = head

        while(temp):
            print(temp.val, end=" -> ")
            temp = temp.next
        print('None')

head = Linkedlist()
solution = Solution()

values_of_node = [10, 20, 30, 40, 50]
for value in values_of_node:
    head.insert_node(value)

roated_list = solution.rotateRight(head.get_head(), 4)

print_linked_list(roated_list)