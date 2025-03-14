#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

/**
 * addTwoNumbers - Adds two numbers represented as linked lists
 * @l1: First linked list
 * @l2: Second linked list
 *
 * Return: Sum represented as a linked list
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *current, *dummyHead, *node;
    int carry = 0, val1, val2, sum;

    // Allocate memory for the dummy head
    dummyHead = (struct ListNode *)malloc(sizeof(struct ListNode));
    if (dummyHead == NULL) {
        return NULL;
    }

    // Initialize dummy head
    dummyHead->val = 0;
    dummyHead->next = NULL;
    current = dummyHead;

    // Traverse and calculate the sum
    while (l1 || l2 || carry) {
        // Get values from the nodes or use 0 if the list has ended
        val1 = (l1 != NULL) ? l1->val : 0;
        val2 = (l2 != NULL) ? l2->val : 0;

        // Compute sum and carry
        sum = val1 + val2 + carry;
        carry = sum / 10;

        // Create a new node for the current digit
        node = (struct ListNode *)malloc(sizeof(struct ListNode));
        if (node == NULL) {
            // Free allocated memory on failure
            while (dummyHead != NULL) {
                struct ListNode *temp = dummyHead;
                dummyHead = dummyHead->next;
                free(temp);
            }
            return NULL;
        }

        // Initialize the node
        node->val = sum % 10;
        node->next = NULL;

        // Append the node to the result list
        current->next = node;
        current = node;

        // Move to the next nodes in the input lists
        if (l1 != NULL) l1 = l1->next;
        if (l2 != NULL) l2 = l2->next;
    }

    // Skip the dummy head and return the actual result
    struct ListNode *result = dummyHead->next;
    free(dummyHead);
    return result;
}
