from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Linkedlist:
    def __init__(self, value):
        self.head = ListNode(value)
    
    def insert_node(self, value):
        node =  ListNode(value)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
    
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print('None')

    def get_head(self):
        return self.head

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        end = head

        while end and end.next:
            middle = middle.next
            end = end.next.next
        
        return middle.val

# test case
solution = Solution()

linkedlist = Linkedlist(3)
linkedlist.insert_node(4)
linkedlist.insert_node(5)
linkedlist.insert_node(6)
linkedlist.insert_node(7)

linkedlist.display()

print(solution.middleNode(linkedlist.get_head()))