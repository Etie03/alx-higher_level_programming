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

