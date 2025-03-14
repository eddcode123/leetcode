#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};


/**
 * mergeTwoLists - Merges two sorted singly linked lists into a single sorted list.
 *
 * This function takes two sorted linked lists, merges them into one sorted
 * linked list, and returns the head of the merged list. The original lists
 * are linked directly to form the merged list, and no additional nodes are created,
 * except for a temporary dummy node used to simplify the merging process.
 *
 * @list1: Pointer to the head of the first sorted linked list.
 * @list2: Pointer to the head of the second sorted linked list.
 *
 * Return: Pointer to the head of the merged sorted linked list.
 *         Returns NULL if both input lists are empty or memory allocation fails.
 *
 * Note:
 * - The function assumes both input lists are already sorted in ascending order.
 * - The dummy node is used temporarily and its memory is freed before returning.
 */

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *current, *dummyHead, *merged;

    /* Allocate memory for a dummy node to simplify the merge logic */
    dummyHead = (struct ListNode *)malloc(sizeof(struct ListNode));
    if (dummyHead == NULL) {
        return (NULL); /* Return NULL if memory allocation fails */
    }

    /* Initialize the dummy node */
    dummyHead->val = 0;
    dummyHead->next = NULL;

    current = dummyHead;

    /* Merge the two linked lists by comparing their nodes */
    while (list1 && list2)
    {
        /* Attach the node with the smaller value to the merged list */
        if (list1->val < list2->val)
        {
            current->next = list1;
            list1 = list1->next; /* Advance the pointer in the first list */
        }
        else
        {
            current->next = list2;
            list2 = list2->next; /* Advance the pointer in the second list */
        }

        /* Move the current pointer forward in the merged list */
        current = current->next;
    }

    /* Attach the remaining nodes from the non-empty list, if any */
    if (list1)
    {
        current->next = list1;
    }
    else
    {
        current->next = list2;
    }

    /* Get the head of the merged list and free the dummy node */
    merged = dummyHead->next;
    free(dummyHead);

    return (merged); /* Return the merged list */
}
