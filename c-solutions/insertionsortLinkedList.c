#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* insertionSortList(struct ListNode* head) {
    
    /* Initialize pointers for traversal and sorting */
    struct ListNode *current, *sorted, *temp, *next;
    current = head;
    sorted = NULL;

    /* Return head if the list is empty or has only one node */
    if (!head || !head->next)
    {
        return (head);
    }

    /* Traverse the list and insert nodes into the sorted portion */
    while (current)
    {
        /* Save the next node to continue traversal later */
        next = current->next;

        /* Insert the current node at the start of the sorted list if necessary */
        if (!sorted || sorted->val >= current->val)
        {
            current->next = sorted;
            sorted = current;
        }
        else
        {
            /* Find the correct position in the sorted list */
            temp = sorted;

             /* Move temp forward until the correct insertion point is found */
            while (temp->next && temp->next->val < current->val)
            {
                temp = temp->next;
            }
            /* Insert the current node between temp and temp->next */
            current->next = temp->next;
            temp->next = current;
        }
        /* Move to the next node in the original list */
        current = next;
    }

     /* Update and return the head pointer to the new sorted list */
    head = sorted;

    return (head);
}