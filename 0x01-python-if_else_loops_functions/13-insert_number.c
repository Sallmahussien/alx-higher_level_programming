#include "lists.h"

/**
 * insert_node - insert a new node in descending order
 * @head: linked list
 * @number: number to be inserted
 * Return: the inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr1 = *head, *ptr2;
	listint_t *node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);
	node->n = number;
	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
		return (node);
	}
	if ((*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while (ptr1)
	{
		ptr2 = ptr1->next;
		if (ptr2 == NULL)
		{
			node->next = NULL;
			ptr1->next = node;
			return (node);
		}
		if (ptr2->n > number)
		{
			node->next = ptr2;
			ptr1->next = node;
			return (node);
		}
		ptr1 = ptr1->next;
	}
	return (node);

}
