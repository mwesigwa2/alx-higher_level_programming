#include "lists.h"

/**
* insert_node - inserts a number into a sorted
* singly linked list
* @head: double pointer to start node
* @number: number to be inserted
* Return: address of new node or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node, *new_node, *previous;

	if (!head)
		return (NULL);
	current_node = *head;
	previous = NULL;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	while (current_node && current_node->n <= number)
	{
		previous = current_node;
		current_node = current_node->next;
	}
	if (previous)
	{
		previous->next = new_node;
		new_node->next = current_node;
	}
	else
	{
		*head = new_node;
		new_node->next = current_node;
	}
	return (new_node);
}

