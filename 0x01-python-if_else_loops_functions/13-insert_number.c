#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
  * insert_node - Inserts a number into a sorted singly linked list
  * @head: The head of the sorted singly linked list
  * @number: The number to inserts in the singly linked list
  *
  * Return: The singly linked list with the new number added
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev_head;

	prev_head = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	
	new_node->n = number;

	if (prev_head == NULL || number < prev_head->n)
	{
		new_node->next = prev_head;
		*head = new_node;
		return (new_node);
	}

	while (prev_head ->next)
	{
		if (prev_head->n <= number && number <= prev_head->next->n)
			{
				new_node->next = prev_head->next;
				prev_head->next = new_node;
				return (new_node);
			}
		prev_head = prev_head->next;
	}
	new_node->next = prev_head->next;
	prev_head->next = new_node;
	return(new_node);
}
