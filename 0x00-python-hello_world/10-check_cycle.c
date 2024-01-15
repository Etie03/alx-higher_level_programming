#include "lists.h"
/**
 * check_cycle - a function that checks if a linked list has a cycle in it
 * @list: pointer to head of list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *m = list;
	listint_t *p = list;

	do {
		if (p == NULL || p->next == NULL)
			return (0);

		m = m->next;
		p = p->next->next;
	} while (m != p);

	return (1);
}
