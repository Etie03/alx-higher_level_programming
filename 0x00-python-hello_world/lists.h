#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_t] - singly linked list
 * @data: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */


typedef struct ListNode
{
	int data;
	struct ListNode *next;
} listint_t;

int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
#endif
